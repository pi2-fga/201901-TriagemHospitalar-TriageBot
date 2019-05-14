## intent:dor_de_cabeca <!--- The label of the intent -->
  - Estou com dor de cabeça
  - Tô com dor de cabeça
  - Dor de cabeça
  - Enxaqueca
  - Estou com enxaqueca
  - Cefaleia

## intent:outros_sintomas <!--- The label of the intent -->
  - nausea
  - Naúsea
  - Enjoo
  - Ânsia
  - Ansia
  - dor no pescoço
  - estou enjoado
  - estou com tontura
  - estou enjoada

## intent: sim
  - sim
  - isso
  - positivo

## intent:negativo
  - não
  - nada

## intent:dados
  - estes são meus dados: (data)

## intent:escala_de_dor
  - nivel de dor: [10](pain_scale)
  - nivel de dor: [9](pain_scale)
  - nivel de dor: [8](pain_scale)
  - nivel de dor: [7](pain_scale)
  - nivel de dor: [6](pain_scale)
  - nivel de dor: [5](pain_scale)
  - nivel de dor: [4](pain_scale)
  - nivel de dor: [3](pain_scale)
  - nivel de dor: [2](pain_scale)
  - nivel de dor: [1](pain_scale)

## intent:persistencia_dor
  - [constante](pain_persistance:constant)
  - [insistente](pain_persistance:constant)
  - [grande](pain_persistance:constant)
  - [muita](pain_persistance:constant)
  - [súbito](pain_persistance:not_constant)
  - [vai e volta](pain_persistance:not_constant)
  - [toda hora](pain_persistance:constant)
  - [progressiva](pain_persistance:not_constant)
  - [de repente]((pain_persistance:not_constant))
  - a dor é [constante](pain_persistance:constant)
  - a dor [não vai embora]((pain_persistance:constant))
