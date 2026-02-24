# FitLife — Contexto del caso

## La empresa

**FitLife** es una red de 5 centros de fitness de proximidad en una ciudad. Espacios pequenos (200-300 m2) en barrios residenciales, con equipamiento de musculacion, zona cardio, sala de clases grupales y app propia. No tienen piscina ni spa. Operacion lean: 1-2 empleados por centro, instructores compartidos.

## Planes de suscripcion

| Plan | Precio |
|------|--------|
| basic | 29 EUR/mes |
| premium | 49 EUR/mes |
| family | 69 EUR/mes |

## El competidor

Una cadena low-cost opera en la misma zona con espacios mas grandes pero sin clases ni atencion personalizada. Este competidor cobraba 25 EUR en 2022 y ha ido bajando precios progresivamente hasta 19 EUR en 2024.

## Posicionamiento

FitLife esta en tierra de nadie. No es low-cost (29 EUR > 19 EUR del competidor), pero tampoco es premium. Su propuesta de valor es proximidad + comunidad + clases grupales, pero el plan basico no incluye gran parte de eso, lo que lo deja expuesto a la comparacion directa con el low-cost.

## El problema

FitLife tiene alta rotacion de socios, con picos de altas en enero que se desinflan rapidamente. El churn del plan basico ha subido significativamente en los ultimos dos anos, mientras que premium y family se mantienen estables.

## Los datos

Dispones de 3 anos de datos (enero 2022 - diciembre 2024) en dos archivos:

### fitlife_members.csv

Tabla principal. Cada fila es un socio en un mes concreto.

| Columna | Descripcion |
|---------|-------------|
| member_id | ID unico del socio |
| month | Mes del registro (YYYY-MM) |
| center | Centro (downtown, northside, eastpark, westfield, southgate) |
| plan | Plan contratado (basic, premium, family) |
| price_paid | Precio pagado ese mes (EUR). Refleja descuentos de canal, por lo que no siempre coincide con el precio base del plan. |
| signup_date | Fecha de alta del socio |
| acquisition_channel | Canal de captacion (walk_in, referral, digital, january_campaign, corporate) |
| tenure_months | Meses que lleva como socio |
| visits_this_month | Visitas al centro ese mes |
| group_classes_attended | Clases grupales ese mes |
| uses_app | Usa la app del gimnasio (True/False) |
| has_personal_trainer | Tiene entrenador personal (True/False) |
| cost_to_serve | Coste variable de atender a ese socio ese mes (EUR) |
| status | Estado al final del mes (active / churned) |
| churn_reason | Motivo de baja (price, competitor, no_use, relocation, personal). Null si activo. |

### fitlife_context.csv

Contexto mensual del negocio. Una fila por mes.

| Columna | Descripcion |
|---------|-------------|
| month | Mes (YYYY-MM) |
| competitor_lowcost_price | Precio del competidor low-cost ese mes (EUR) |
| campaign_active | Campana activa (january_promo, back_to_gym, summer_body, o vacio) |
| service_incident | Incidencia de servicio (heating_failure, equipment_breakdown, app_outage, o vacio) |
| monthly_fixed_costs | Costes fijos mensuales totales de la red (EUR) |
| avg_occupancy_rate | Tasa de ocupacion media de los centros (0-1) |
| acquisition_cost_avg | Coste medio de adquisicion de un nuevo socio ese mes (EUR) |

Las dos tablas se relacionan por la columna `month`.

## La pregunta

> El churn del plan basico ha subido significativamente en los ultimos dos anos, mientras que premium y family se mantienen estables. El competidor low-cost cobra 19 EUR y FitLife cobra 29 EUR por el plan basico.
>
> **Deberia FitLife bajar el precio del plan basico?**

Esta es la pregunta que guiara todo el taller. No tiene una respuesta unica.
