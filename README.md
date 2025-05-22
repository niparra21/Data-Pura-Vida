# Data-Pura-Vida

## 1. Evaluación de Riesgos

## 1.1 Identificacion de riesgos

### Riesgos técnicos:
| ID  | Riesgo                                       | Descripcion                                                             |
| --- | -------------------------------------------- | ----------------------------------------------------------------------- |
| T01 | incompatibilidad de formatos                 | dificultad para procesar datasets de diversos formatos (CSV, JSON, XML) |
| T02 | fallos en enfoques de procesamiento de datos | perdida o corrupcion de datos durante transformaciones                  |
| T03 | escalabilidad del Data Lake                  | limitaciones en almacenamiento/consulta con crecimiento de datos        |
| T04 | rendimiento de visualizaciones               | latencias altas en dashboards complejos / alto trafico                  |
| T05 | integración con sistemas legacy              | incompatibilidad con APIs/bases de datos de instituciones publicas      |
| T06 | disponibilidad del sistema                   | caidas cuando haya alta demanda                                         |
| T07 | complejidad de la IA                         | la implementacion tenga baja precision                                  |

### Riesgos de seguridad:
| ID  | Riesgo                     | Descripcion                                                        |
| --- | -------------------------- | ------------------------------------------------------------------ |
| S01 | brechas de datos sensibles | exposicion accidental de informacion personal/confidencial         |
| S02 | gestion de identidad       | fallos en autenticacion MFA o suplantacion de identidad            |
| S03 | cifrado inadecuado         | vulnerabilidad de los datos que se encuentran en reposo / transito |
| S04 | privilegio de accesos      | abusos de permisos de administrador                                |
| S05 | falta de auditoria         | insuficiencia en trazabilida de accesos / cambios                  |

### Riesgos legales y cumplimiento:
| ID  | Riesgo                  | Descripcion                                                   |
| --- | ----------------------- | ------------------------------------------------------------- |
| L01 | incumplimiento de leyes | sanciones por el manejo inadecuado de la informacion personal |
| L02 | propiedad de data       | disputas acerca del derecho de datasets compartidos           |

### Riesgos operacionales:
| ID  | Riesgo                     | Descripcion                                                          |
| --- | -------------------------- | -------------------------------------------------------------------- |
| O01 | resistencia a cambio       | rechazo por parte de instituciones o individuos                      |
| O02 | dependencia en proveedores | Cloud outages (interrupciones en la nube) o cambios en APIs criticos |

### Riesgos financieros:
| ID  | Riesgo                         | Descripcion                                  |
| --- | ------------------------------ | -------------------------------------------- |
| F01 | altos costos operativos        | infraestructura mas cara de lo presupuestado |
| F02 | modelo de monetizacion fallido | adopcion baja de los datasets de pago        |

### Riesgos de calidad:
| ID  | Riesgo                          | Descripcion                                                 |
| --- | ------------------------------- | ----------------------------------------------------------- |
| C01 | incoinsistencia de datos        | errores en las fuentes, lo cual afecta el analisis          |
| C02 | falta de metadata               | dificulta la interpretaciond de datasets por parte de la IA |
| C03 | problemas con interoperabilidad | datasets que no se puedan relacionar entre si               |

## 1.2 Analisis de riesgos y evaluacion de los riesgos
Con base en probabilidad (porcentaje) x impacto (menor, medio, mayor, critico) se puede definir que riesgos son los que se deban priorizar

| Nivel        | Criterios                           | Riesgos Asociados                      | Tratamiento            | Acciones a tomar                                                                                                                                                                                                              |
| ------------ | ----------------------------------- | -------------------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Crítico**  | Probabilidad >70% + Impacto Crítico | S01, L01, T02                          | Mitigación inmediata   | - Implementar cifrado + validacion de tokens (S01)<br>- Auditoría legal  (L01)<br>- Pipeline con validacion en multiples fases (T02)                                                                                                  |
| **Alto**     | Probabilidad 30-70% + Impacto Mayor | T01, T03, S02, S03, O01                | Mitigación planificada | - Estandarización de diversos formatos (T01)<br>- Autoescalado con base en la demanda (T03)<br>- Revisión de permisos (S02/S03)<br>- Generacion de casos de exito y demostracion de beneficios (O01)                          |
| **Moderado** | Probabilidad 10-30% + Impacto Medio | T04, T05, S04, F01, C01                | Monitoreo activo       | - Cache de visualizaciones (T04)<br>- mecanismos de adaptación para APIs legacy (como middleware) (T05)<br>- Alertas por uso de privilegios (S04)<br>- Modelo de costos dinámico (F01)<br>- Validación cruzada de datos (C01) |
| **Bajo**     | Probabilidad <10% + Impacto Menor   | T06, T07, S05, L02, O02, F02, C02, C03 | Aceptación controlada  | - Documentar en registro de riesgos<br>- Incluir en revisiones                                                                                                                                                                |

