"""
FitLife Analytics Dashboard
Taller MDA13 — Analítica Conversacional con GenAI

Baseline: dashboard determinista con filtros y visualizaciones.
Sin IA. Esta es la versión que los alumnos reciben al inicio de la sesión 1.
"""

import streamlit as st
import pandas as pd

# ---------------------------------------------------------------------------
# Configuración de página
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="FitLife Analytics",
    page_icon="🏋️",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Carga de datos (cacheada)
# ---------------------------------------------------------------------------
@st.cache_data
def load_data():
    members = pd.read_csv("data/fitlife_members.csv")
    context = pd.read_csv("data/fitlife_context.csv")
    return members, context

members, context = load_data()

# ---------------------------------------------------------------------------
# Sidebar — Filtros
# ---------------------------------------------------------------------------
st.sidebar.header("Filtros")

# Rango de meses
all_months = sorted(members["month"].unique())
month_start, month_end = st.sidebar.select_slider(
    "Periodo",
    options=all_months,
    value=(all_months[0], all_months[-1]),
)

# Centro
centers = st.sidebar.multiselect(
    "Centro",
    options=sorted(members["center"].unique()),
    default=sorted(members["center"].unique()),
)

# Plan
plans = st.sidebar.multiselect(
    "Plan",
    options=sorted(members["plan"].unique()),
    default=sorted(members["plan"].unique()),
)

# ---------------------------------------------------------------------------
# Aplicar filtros
# ---------------------------------------------------------------------------
mask = (
    (members["month"] >= month_start)
    & (members["month"] <= month_end)
    & (members["center"].isin(centers))
    & (members["plan"].isin(plans))
)
df = members[mask].copy()

# ---------------------------------------------------------------------------
# Título
# ---------------------------------------------------------------------------
st.title("FitLife Analytics Dashboard")
st.caption(f"Datos filtrados: {len(df):,} registros · {df['member_id'].nunique():,} socios únicos")

# ---------------------------------------------------------------------------
# KPIs principales
# ---------------------------------------------------------------------------
latest_month = df["month"].max()
df_latest = df[df["month"] == latest_month]

col1, col2, col3, col4 = st.columns(4)

with col1:
    active_count = df_latest[df_latest["status"] == "active"].shape[0]
    st.metric("Socios activos", f"{active_count:,}", help=f"En {latest_month}")

with col2:
    churned_count = df_latest[df_latest["status"] == "churned"].shape[0]
    total_count = df_latest.shape[0]
    churn_rate = churned_count / total_count * 100 if total_count > 0 else 0
    st.metric("Tasa de churn", f"{churn_rate:.1f}%", help=f"Bajas / total en {latest_month}")

with col3:
    revenue = df_latest["price_paid"].sum()
    st.metric("Ingresos mes", f"{revenue:,.0f} EUR", help=f"Suma price_paid en {latest_month}")

with col4:
    avg_visits = df_latest["visits_this_month"].mean()
    st.metric("Visitas/socio", f"{avg_visits:.1f}", help=f"Media en {latest_month}")

st.divider()

# ---------------------------------------------------------------------------
# Gráficos — fila 1
# ---------------------------------------------------------------------------
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Socios activos por mes")
    active_by_month = (
        df[df["status"] == "active"]
        .groupby("month")["member_id"]
        .nunique()
        .reset_index(name="socios_activos")
    )
    st.line_chart(active_by_month, x="month", y="socios_activos", height=300)

with col_right:
    st.subheader("Tasa de churn mensual por plan")
    # Calcular churn rate por plan y mes
    churn_by_plan = (
        df.groupby(["month", "plan"])
        .agg(total=("member_id", "count"), churned=("status", lambda x: (x == "churned").sum()))
        .reset_index()
    )
    churn_by_plan["churn_rate"] = churn_by_plan["churned"] / churn_by_plan["total"] * 100

    # Pivotear para st.line_chart
    churn_pivot = churn_by_plan.pivot(index="month", columns="plan", values="churn_rate").reset_index()
    st.line_chart(churn_pivot, x="month", y=[c for c in churn_pivot.columns if c != "month"], height=300)

# ---------------------------------------------------------------------------
# Gráficos — fila 2
# ---------------------------------------------------------------------------
col_left2, col_right2 = st.columns(2)

with col_left2:
    st.subheader("Distribución por plan")
    plan_dist = df_latest.groupby("plan")["member_id"].count().reset_index(name="socios")
    st.bar_chart(plan_dist, x="plan", y="socios", height=300)

with col_right2:
    st.subheader("Distribución por centro")
    center_dist = df_latest.groupby("center")["member_id"].count().reset_index(name="socios")
    st.bar_chart(center_dist, x="center", y="socios", height=300)

# ---------------------------------------------------------------------------
# Gráficos — fila 3
# ---------------------------------------------------------------------------
col_left3, col_right3 = st.columns(2)

with col_left3:
    st.subheader("Ingresos mensuales")
    revenue_by_month = df.groupby("month")["price_paid"].sum().reset_index(name="ingresos")
    st.line_chart(revenue_by_month, x="month", y="ingresos", height=300)

with col_right3:
    st.subheader("Motivos de baja")
    churn_reasons = (
        df[df["status"] == "churned"]
        .groupby("churn_reason")["member_id"]
        .count()
        .reset_index(name="bajas")
        .sort_values("bajas", ascending=False)
    )
    st.bar_chart(churn_reasons, x="churn_reason", y="bajas", height=300)

# ---------------------------------------------------------------------------
# Tabla de contexto (colapsable)
# ---------------------------------------------------------------------------
with st.expander("Contexto del negocio (datos mensuales del mercado)"):
    ctx_filtered = context[
        (context["month"] >= month_start) & (context["month"] <= month_end)
    ]
    st.dataframe(ctx_filtered, use_container_width=True, hide_index=True)

# ---------------------------------------------------------------------------
# Vista de datos crudos (colapsable)
# ---------------------------------------------------------------------------
with st.expander("Ver datos crudos"):
    st.dataframe(df.head(200), use_container_width=True, hide_index=True)
