## intent:dor_de_cabeca <!--- The label of the intent -->
  - Estou com dor de cabeça
  - Tô com dor de cabeça
  - Dor de cabeça
  - Enxaqueca
  - Estou com enxaqueca
  - Cefaleia
  - dor de cabeça e enjoo

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
  - dor na nuca

## intent: sim
  - sim
  - isso
  - positivo

## intent:negativo
  - não
  - nada
  - nadinha
  - de forma alguma

## intent:dados
  - estes são meus sinais vitais (data)

## intent:escala_de_dor
  - [dez](pain_scale:10)
  - [nove](pain_scale:9)
  - [oito](pain_scale:8)
  - [sete](pain_scale:7)
  - [seis](pain_scale:6)
  - [cinco](pain_scale:5)
  - [quatro](pain_scale:4)
  - [tres](pain_scale:3)
  - [dois](pain_scale:2)
  - [um](pain_scale:1)

## intent:persistencia_dor
  - [constante](pain_persistance:constant)
  - [insistente](pain_persistance:constant)
  - [grande](pain_persistance:constant)
  - [muita](pain_persistance:constant)
  - [súbito](pain_persistance:not_constant)
  - [vai e volta](pain_persistance:not_constant)
  - [toda hora](pain_persistance:constant)
  - [progressiva](pain_persistance:not_constant)
  - [de repente](pain_persistance:not_constant)
  - a dor é [constante](pain_persistance:constant)
  - a dor [não vai embora](pain_persistance:constant)
  - a dor [não para](pain_persistance:constant)

## intent:intoxicacao
  - eu tomei (substancia)
  - eu engoli (substancia)
  - tomei (substancia)
  - engoli (substancia)
  - tomei uma caixa de (substancia)
  - eu tomei veneno
  - tomei mais comprimidos do que deveria
  - tomei muito comprimido
  - tomei a dosagem errada do meu remédio
  - tomei a dosagem errada
  - eu confundi o remédio
  - confundi o remédio
  - confundi meu remédio
  - inalei produto de limpeza
  - respirei muito produto de limpeza
  - inalei (substancia)
  - respirei (substancia)

## intent:idade
 - Qual é a sua idade? (age)
 - Qual é a sua idade? Minha idade é (age)
 - Qual é a sua idade? Tenho (age) anos
 - Qual é a sua idade? Tenho (age)

## intent:medicacao
 - Você usa medicação contínua? Se sim, cite quais.  [Não](continuos_medication) uso
 - Você usa medicação contínua? Se sim, cite quais.  [não](continuos_medication) uso
 - Você usa medicação contínua? Se sim, cite quais.  [Não] (continuos_medication)
 - Você usa medicação contínua? Se sim, cite quais.  [Não] (continuos_medication) tomo remédio
 - Você usa medicação contínua? Se sim, cite quais.  [Não] (continuos_medication) tomo
 - Você usa medicação contínua? Se sim, cite quais.  Sim uso (continuos_medication)
 - Você usa medicação contínua? Se sim, cite quais.  Sim tomo (continuos_medication)
 - Você usa medicação contínua? Se sim, cite quais.  Tomo (continuos_medication)
 - Você usa medicação contínua? Se sim, cite quais. (continuous_medication)

##intent:alergias
- Você possui alergia a alguma medicação? Se sim, cite a quais. (alergies)
