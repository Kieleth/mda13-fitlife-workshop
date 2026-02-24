# FitLife | Enunciado

---

## Contexto

**FitLife** es una red de 5 centros de fitness de proximidad en una ciudad. Espacios pequeños (200-300 m2) en barrios residenciales, con equipamiento de musculación, zona cardio, sala de clases grupales y app propia. No tienen piscina ni spa. Operación lean: 1-2 empleados por centro, instructores compartidos.

Ofrecen tres planes de suscripción mensual:

| Plan | Precio |
|------|--------|
| basic | 29 EUR/mes |
| premium | 49 EUR/mes |
| family | 69 EUR/mes |

Su principal competidor es una cadena low-cost que opera en la misma zona con espacios más grandes pero sin clases ni atención personalizada. Este competidor cobraba 25 EUR en 2022 y ha ido bajando precios progresivamente hasta 19 EUR en 2024.

**Posicionamiento:** FitLife está en tierra de nadie. No es low-cost (29 EUR > 19 EUR del competidor), pero tampoco es premium. Su propuesta de valor es proximidad + comunidad + clases grupales, pero el plan básico no incluye gran parte de eso, lo que lo deja expuesto a la comparación directa con el low-cost.

FitLife tiene un problema habitual del sector: alta rotación de socios, con picos de altas en enero que se desinflan rápidamente.

Dispones de 3 años de datos (enero 2022 - diciembre 2024).

---

## Datos

### fitlife_members.csv

Tabla principal. Cada fila representa un socio en un mes concreto.

| Columna | Descripción |
|---------|-------------|
| member_id | ID único del socio |
| month | Mes del registro (YYYY-MM) |
| center | Centro (downtown, northside, eastpark, westfield, southgate) |
| plan | Plan contratado (basic, premium, family) |
| price_paid | Precio pagado ese mes (EUR) |
| signup_date | Fecha de alta del socio |
| acquisition_channel | Canal por el que se captó al socio (walk_in, referral, digital, january_campaign, corporate) |
| tenure_months | Meses que lleva como socio |
| visits_this_month | Visitas al centro ese mes |
| group_classes_attended | Clases grupales ese mes |
| uses_app | Usa la app del gimnasio (True/False) |
| has_personal_trainer | Tiene entrenador personal (True/False) |
| cost_to_serve | Coste variable de atender a ese socio ese mes (EUR) |
| status | Estado al final del mes (active / churned) |
| churn_reason | Motivo de baja (price, competitor, no_use, relocation, personal). Null si sigue activo. |

### fitlife_context.csv

Contexto mensual del negocio. Una fila por mes.

| Columna | Descripción |
|---------|-------------|
| month | Mes (YYYY-MM) |
| competitor_lowcost_price | Precio del competidor low-cost ese mes (EUR) |
| campaign_active | Campaña de captación activa ese mes (january_promo, back_to_gym, summer_body, o vacío) |
| service_incident | Incidencia de servicio relevante ese mes (heating_failure, equipment_breakdown, app_outage, o vacío) |
| monthly_fixed_costs | Costes fijos mensuales totales de la red de centros (EUR) |
| avg_occupancy_rate | Tasa de ocupación media de los centros (0-1) |
| acquisition_cost_avg | Coste medio de adquisición de un nuevo socio ese mes (EUR) |

Las dos tablas se pueden relacionar por la columna `month`.

---

## Pregunta

El churn del plan básico ha subido significativamente en los últimos dos años, mientras que premium y family se mantienen estables. El competidor low-cost cobra 19 EUR y FitLife cobra 29 EUR por el plan básico.

> **¿Debería FitLife bajar el precio del plan básico?**

Esta es la pregunta que guiará todo el taller. No tiene una respuesta única.
