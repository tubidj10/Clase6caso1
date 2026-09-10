# Proceso documentado

Construcción docente en una sesión; no se atribuyen despliegues ni revisiones humanas inexistentes.

## Decisión 1: cantidades fuera del modelo
Se calculan con código y se entrega la observación al LLM para que explique la propuesta. La respuesta se valida contra el cálculo antes de considerarse utilizable. Esto evita que un JSON bien formado se confunda con una cantidad correcta.

## Decisión 2: corregir la primera fórmula considerada
La alternativa inicial omitía pedidos entrantes y bultos. proceso/comparacion_formulas.json conserva la comparación efectivamente calculada: para el primer artículo la fórmula inicial proponía 9 y la seleccionada propone 10; en el segundo escenario habría propuesto 9 cuando ya hay 12 unidades entrantes y no debe comprarse. No se presenta como un error descubierto en producción. Se eligió la fórmula completa antes de generar las corridas.

## Decisión 3: no completar el plazo ausente
El escenario 03 carece de lead_days en RES-04. La herramienta devuelve cantidad nula y revisión manual. El contrato exige preservar ese resultado.

## Evidencia y limitaciones de la historia
Las pruebas guardadas muestran verificaciones realizadas sobre los archivos incluidos. El historial Git permite ubicar implementación y documentación. No se conserva una conversación completa con la IA ni una validación de campo empresarial. Las corridas preservan las instrucciones efectivamente enviadas al modelo; esas sí pueden auditarse literalmente.
