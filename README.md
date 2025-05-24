# Data-Pura-Vida

## 1. Evaluación de Riesgos

### 1.1 Identificacion de riesgos

#### Riesgos técnicos:
| ID  | Riesgo                                       | Descripcion                                                             |
| --- | -------------------------------------------- | ----------------------------------------------------------------------- |
| T01 | incompatibilidad de formatos                 | dificultad para procesar datasets de diversos formatos (CSV, JSON, XML) |
| T02 | fallos en enfoques de procesamiento de datos | perdida o corrupcion de datos durante transformaciones                  |
| T03 | escalabilidad del Data Lake                  | limitaciones en almacenamiento/consulta con crecimiento de datos        |
| T04 | rendimiento de visualizaciones               | latencias altas en dashboards complejos / alto trafico                  |
| T05 | integración con sistemas legacy              | incompatibilidad con APIs/bases de datos de instituciones publicas      |
| T06 | disponibilidad del sistema                   | caidas cuando haya alta demanda                                         |
| T07 | complejidad de la IA                         | la implementacion tenga baja precision                                  |

#### Riesgos de seguridad:
| ID  | Riesgo                     | Descripcion                                                        |
| --- | -------------------------- | ------------------------------------------------------------------ |
| S01 | brechas de datos sensibles | exposicion accidental de informacion personal/confidencial         |
| S02 | gestion de identidad       | fallos en autenticacion MFA o suplantacion de identidad            |
| S03 | cifrado inadecuado         | vulnerabilidad de los datos que se encuentran en reposo / transito |
| S04 | privilegio de accesos      | abusos de permisos de administrador                                |
| S05 | falta de auditoria         | insuficiencia en trazabilida de accesos / cambios                  |

#### Riesgos legales y cumplimiento:
| ID  | Riesgo                  | Descripcion                                                   |
| --- | ----------------------- | ------------------------------------------------------------- |
| L01 | incumplimiento de leyes | sanciones por el manejo inadecuado de la informacion personal |
| L02 | propiedad de data       | disputas acerca del derecho de datasets compartidos           |

#### Riesgos operacionales:
| ID  | Riesgo                     | Descripcion                                                          |
| --- | -------------------------- | -------------------------------------------------------------------- |
| O01 | resistencia a cambio       | rechazo por parte de instituciones o individuos                      |
| O02 | dependencia en proveedores | Cloud outages (interrupciones en la nube) o cambios en APIs criticos |

#### Riesgos financieros:
| ID  | Riesgo                         | Descripcion                                  |
| --- | ------------------------------ | -------------------------------------------- |
| F01 | altos costos operativos        | infraestructura mas cara de lo presupuestado |
| F02 | modelo de monetizacion fallido | adopcion baja de los datasets de pago        |

#### Riesgos de calidad:
| ID  | Riesgo                          | Descripcion                                                 |
| --- | ------------------------------- | ----------------------------------------------------------- |
| C01 | incoinsistencia de datos        | errores en las fuentes, lo cual afecta el analisis          |
| C02 | falta de metadata               | dificulta la interpretaciond de datasets por parte de la IA |
| C03 | problemas con interoperabilidad | datasets que no se puedan relacionar entre si               |

### 1.2 Analisis de riesgos y evaluacion de los riesgos
Con base en probabilidad (porcentaje) x impacto (menor, medio, mayor, critico) se puede definir que riesgos son los que se deban priorizar

| Nivel        | Criterios                           | Riesgos Asociados                      | Tratamiento            | Acciones a tomar                                                                                                                                                                                                              |
| ------------ | ----------------------------------- | -------------------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Crítico**  | Probabilidad >70% + Impacto Crítico | S01, L01, T02                          | Mitigación inmediata   | - Implementar cifrado + validacion de tokens (S01)<br>- Auditoría legal  (L01)<br>- Pipeline con validacion en multiples fases (T02)                                                                                                  |
| **Alto**     | Probabilidad 30-70% + Impacto Mayor | T01, T03, S02, S03, O01                | Mitigación planificada | - Estandarización de diversos formatos (T01)<br>- Autoescalado con base en la demanda (T03)<br>- Revisión de permisos (S02/S03)<br>- Generacion de casos de exito y demostracion de beneficios (O01)                          |
| **Moderado** | Probabilidad 10-30% + Impacto Medio | T04, T05, S04, F01, C01                | Monitoreo activo       | - Cache de visualizaciones (T04)<br>- mecanismos de adaptación para APIs legacy (como middleware) (T05)<br>- Alertas por uso de privilegios (S04)<br>- Modelo de costos dinámico (F01)<br>- Validación cruzada de datos (C01) |
| **Bajo**     | Probabilidad <10% + Impacto Menor   | T06, T07, S05, L02, O02, F02, C02, C03 | Aceptación controlada  | - Documentar en registro de riesgos<br>- Incluir en revisiones                                       

---
## Leyes y Estándares Relevantes para la Plataforma **Data Pura Vida**

### Ley 8968 - Ley de Protección de la Persona frente al Tratamiento de sus Datos Personales (Costa Rica)

#### ¿Qué es?

La **Ley 8968**, publicada en Costa Rica, establece el marco legal para la protección de los datos personales de los individuos. Esta ley garantiza los derechos fundamentales de las personas respecto al tratamiento de su información personal, asegurando su privacidad y control sobre sus datos.

#### Aplicación en el proyecto

- **Registro de usuarios**: Al recopilar información personal y documentos de identificación, es crítico obtener el consentimiento explícito de los usuarios y garantizar la transparencia en el uso de sus datos.
- **Módulo "Feliz compartiendo datos"**: Debe permitir a los usuarios decidir qué datos compartir, con quién y bajo qué condiciones, respetando su autonomía y privacidad.
- **Protección de datos sensibles**: Implementar medidas técnicas y organizativas para proteger la información sensible, como cifrado y controles de acceso.

#### Módulos clave

- **Bio Registro Verde**: Debe incluir mecanismos para obtener y registrar el consentimiento informado de los usuarios.
- **Feliz compartiendo datos**: Herramientas para que los usuarios gestionen sus preferencias de privacidad y compartición de datos.
- **Backoffice**: Funcionalidades para evaluar el cumplimiento de la ley y gestionar solicitudes de acceso, modificación o eliminación de datos.



### Reglamento General de Protección de Datos (GDPR)

#### ¿Qué es?

El **GDPR** es una normativa de la Unión Europea que establece directrices sobre la recopilación y procesamiento de datos personales de individuos dentro de la UE. Aunque Costa Rica no es miembro de la UE, el GDPR se considera un estándar internacional en protección de datos.

#### Aplicación en el proyecto

- **Consentimiento explícito**: Asegurar que los usuarios comprendan y acepten cómo se utilizarán sus datos.
- **Derechos de los usuarios**: Facilitar el acceso, modificación, eliminación y portabilidad de los datos personales.
- **Notificación de brechas de seguridad**: Establecer protocolos para informar a las autoridades y a los usuarios en caso de violaciones de seguridad.

#### Módulos clave

- **Bio Registro Verde**: Implementar procesos claros para la obtención y gestión del consentimiento.
- **Backoffice**: Herramientas para gestionar y responder a las solicitudes de los usuarios relacionadas con sus derechos bajo el GDPR.
- **Pura Vida Data Lake**: Sistemas de monitoreo y alerta para detectar y responder a posibles brechas de seguridad.



### ISO/IEC 27001 - Sistema de Gestión de Seguridad de la Información

#### ¿Qué es?

La **ISO/IEC 27001** es una norma internacional que proporciona un marco para establecer, implementar, mantener y mejorar continuamente un sistema de gestión de seguridad de la información. Su objetivo es proteger la confidencialidad, integridad y disponibilidad de la información.

#### Aplicación en el proyecto

- **Gestión de riesgos**: Identificar y mitigar riesgos relacionados con la seguridad de la información.
- **Controles de seguridad**: Implementar políticas y procedimientos para proteger la información contra accesos no autorizados, pérdida o daño.
- **Auditorías internas**: Realizar evaluaciones periódicas para asegurar el cumplimiento de la norma y mejorar continuamente.

#### Módulos clave

- **Pura Vida Data Lake**: Implementar controles de acceso, cifrado y monitoreo continuo para proteger los datos almacenados.
- **Backoffice**: Herramientas para la gestión de incidentes, auditorías y revisión de políticas de seguridad.
- **API Backend**: Asegurar que todas las interfaces de programación cumplan con los estándares de seguridad establecidos por la norma.



### Gobernanza de Datos según la OCDE

#### ¿Qué es?

La **Organización para la Cooperación y el Desarrollo Económicos (OCDE)** promueve principios y buenas prácticas en la gobernanza de datos, enfocándose en la gestión responsable y ética de los datos a lo largo de su ciclo de vida. Esto incluye aspectos como la calidad de los datos, la transparencia, la privacidad y la interoperabilidad.

#### Aplicación en el proyecto

- **Interoperabilidad**: Facilitar el intercambio de datos entre diferentes entidades y sistemas de manera eficiente y segura.
- **Transparencia**: Proporcionar información clara sobre cómo se recopilan, procesan y utilizan los datos.
- **Calidad de los datos**: Implementar mecanismos para asegurar que los datos sean precisos, completos y actualizados.

#### Módulos clave

- **Feliz compartiendo datos**: Herramientas para la estandarización y validación de los datos compartidos por los usuarios.
- **Descubriendo Costa Rica**: Interfaces que permitan a los usuarios explorar y comprender los datos disponibles, promoviendo la transparencia.
- **Pura Vida Data Lake**: Sistemas que aseguren la integridad y calidad de los datos almacenados, facilitando su uso y reutilización.

### Proyecto de Ley de Regulación de la Inteligencia Artificial en Costa Rica

#### ¿Qué es?

El **Proyecto de Ley de Regulación de la Inteligencia Artificial en Costa Rica**, identificado como Expediente N.º 23.771, busca establecer un marco legal para el desarrollo, implementación y uso ético, seguro y sostenible de la inteligencia artificial (IA) en el país. Esta iniciativa se centra en la protección y promoción de la dignidad, los derechos humanos y el bienestar de las personas, en concordancia con la Constitución Política de 1949 y los tratados internacionales de los que Costa Rica es parte.

#### Aplicación en el proyecto

- **Desarrollo ético de IA**: Asegurar que los sistemas de IA utilizados en la plataforma respeten principios éticos, evitando sesgos y discriminación.
- **Transparencia y explicabilidad**: Implementar mecanismos que permitan a los usuarios entender cómo y por qué la IA toma determinadas decisiones.
- **Protección de datos personales**: Garantizar que el tratamiento de datos por parte de sistemas de IA cumpla con las normativas de privacidad y seguridad.
- **Supervisión y responsabilidad**: Establecer procesos para la supervisión humana de las decisiones automatizadas y definir responsabilidades claras en caso de errores o malfuncionamientos.

#### Módulos clave

- **Bio Registro Verde**: Incorporar validaciones éticas en los procesos de registro y verificación de identidad mediante IA.
- **Feliz compartiendo datos**: Asegurar que las recomendaciones y análisis generados por IA sean transparentes y comprensibles para los usuarios.
- **Descubriendo Costa Rica**: Implementar algoritmos de IA que respeten la privacidad y proporcionen explicaciones claras sobre los resultados presentados.
- **Backoffice**: Desarrollar herramientas para la auditoría y supervisión de los sistemas de IA, permitiendo la detección y corrección de posibles sesgos o errores.
  
---

