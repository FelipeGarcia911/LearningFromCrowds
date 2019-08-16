# Learning From Crowds
## Universidad Nacional de Colombia - Facultad de Minas
## Maestria en Ingenieria de Sistemas - Inteligencia Artificial

Este trabajo pretende abordar la problemática de la multiplicidad de formas y fuentes de información
desde la perspectiva del aprendizaje de máquina; más específicamente del tema de clasificación con
múltiples anotadores, en donde la característica principal de este tipo de problemas es que dado un
experimento con sus respectivas atributos, se cuenta con múltiples etiquetas provenientes de diferentes
fuentes o expertos con diferentes niveles de experticia.

## Objetivos del Proyecto

### General
- Evaluar comparativamente los algoritmos más relevantes del estado del arte con respecto a la
clasificación binaria con múltiples anotadores.
### Específicos
- Seleccionar e implementar los algoritmos más relevantes de aprendizaje supervisado con
múltiples anotadores del estado del arte.
- Seleccionar las bases de datos que se van a usar en la evaluación comparativa.
- Evaluar el rendimiento de los métodos implementados en términos de precisión y área bajo la
curva (ROC).

## Técnicas Implementadas

1. Raykar, V. C., Yu, S., Zhao, L. H., Valadez, G. H., Florin, C., Bogoni, L., &amp; Moy, L. (2010).
Learning from crowds. Journal of Machine Learning Research, 11(Apr), 1297-1322.
Citaciones: 921 - Google Scholar. 20 Abril 2019.
Lenguajes disponibles del Algoritmo: MatLab y Julia.

2. Rodrigues, F., Pereira, F., &amp; Ribeiro, B. (2013). Learning from multiple annotators:
distinguishing good from random labelers. Pattern Recognition Letters, 34(12), 1428-1436.
Citaciones: 54 - Google Scholar. 20 Abril 2019.
Lenguajes disponibles del algoritmo: MatLab y Julia.

3. Yan, Y., Rosales, R., Fung, G., Schmidt, M., Hermosillo, G., Bogoni, L., ... &amp; Dy, J. (2010,
March). Modeling annotator expertise: Learning when everybody knows a bit of something. In
Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics
(pp. 932-939).
Citaciones: 186 - Google Scholar. 20 Abril 2019.
Lenguajes disponibles del algoritmo: MatLab.

4. Zhang, J., Wu, X., &amp; Shengs, V. S. (2015). Active learning with imbalanced multiple noisy
labeling. IEEE transactions on cybernetics, 45(5), 1095-1107.
Citaciones: 30 - Google Scholar. 20 Abril 2019.
Lenguajes disponibles del algoritmo: MatLab.

5. Gil-Gonzalez, J., Alvarez-Meza, A., &amp; Orozco-Gutierrez, A. (2018). Learning from multiple
annotators using kernel alignment. Pattern Recognition Letters, 116, 150-156.
Citaciones: 0 - Google Scholar. 20 Abril 2019.
Lenguajes disponibles del Algoritmo: MatLab.

## Conclusiones

1. Como se demuestra en este trabajo y en [16], es posible implementar en Python un conjunto de
algoritmos de aprendizaje de máquina con múltiples anotadores teniendo como referencia los
códigos en MatLab que los autores han proporcionado en sus trabajos.

2. Es posible replicar en código algunos de los algoritmos de clasificación binaria con múltiples
anotadores más relevantes en la literatura.

3. Es posible desarrollar un comparativo no solo básico, sino utilizando métricas mas robustas como
Recall, F1 Score y ROC, las cuales ofrecen al usuario una visión general de cuál técnica usar
según su problema de crowdsourcing entre las diferentes técnicas de clasificación binaria con
múltiples anotadores.

4. Los modelos de aprendizaje de máquina con múltiples anotadores han venido aumentados su
popularidad e importancia a través de los años y más ahora con el crecimiento de la información
de múltiples fuentes y nacimiento de plataformas como Amazon Mechanical Turkey que
permiten de manera sencilla, ágil y económica la recolección de información de muchas
personas.

5. Los autores citados en este documento han presentado diferentes soluciones a los múltiples
problemas que puede acarrear el manejo de múltiples anotadores, algunos han presentados
modelos de variables latentes que modelan la experticia variante entre experimentos de cada
anotador mientras otros presentan propuesta con algunas relajaciones de estas suposiciones.

6. Los autores de [9] y [12], que implementan modelos que usan algoritmos como el EM para
solucionar problemas de optimización donde se busca la máxima verosimilitud de una matriz de
coeficientes y de este modo, determina la experticia de cada uno de los anotadores, han probado
tener mejores resultados que implementaciones más heurísticas como [7], donde se asumen
supuestos que hacen que el modelo propuesto sea sensible al balanceo de clases.

7. Las diferentes técnicas de pre-procesamiento de datos como Selección de Características
permiten manejar el problema de la alta dimensionalidad en conjuntos de datos, ya que se pueden
seleccionar sólo las variables más significativas para el proceso.

8. No es recomendable que el rendimiento de un modelo de aprendizaje de máquina supervisado sea
evaluado sólo con una métrica de rendimiento, esto debido a que métricas como la Precisión
hacen un resumen general del comportamiento del modelo y no permiten visualizar detalles que
pueden indicar que el modelo esté sesgado hacia una clase u otra.

9. Un modelo de clasificación binaria sobre una Regresión Lineal es algo bastante sencillo y rápido
de probar e implementar que puede ser usado para una gran cantidad de tareas sin ningún
problema y con una alta eficiencia, sin embargo existen algunos problemas de clasificación en
donde las clases no pueden ser separadas por hiperplanos, situación en la cual este modelo debe
ser reemplazado por uno más complejo.

10. La implementación en Python de todos estos modelos de aprendizaje de máquina con múltiples
anotadores permitirá a los estudiantes e investigadores contar con nuevas herramientas para
abordar este tipo de problemas.

## BIBLIOGRAFIA

[1] U. Fayyad, G. Piatetsky-Shapiro and P. Smyth, &quot;The KDD process for extracting useful knowledge
from volumes of data&quot;, Communications of the ACM, vol. 39, no. 11, pp. 27-34, 1996.

[2] F. Rodrigues, F. Pereira and B. Ribeiro, &quot;Learning from multiple annotators: Distinguishing good
from random labelers&quot;, Pattern Recognition Letters, vol. 34, no. 12, pp. 1428-1436, 2013.

[3] R. Filipe, &quot;Probabilistic Models for Learning from Crowdsourced Data.&quot;, ResearchGate, 2016.

[4] Rodrigues, Filipe, and Francisco Pereira. &quot;Deep learning from crowds.&quot; arXiv preprint
arXiv:1709.01779 (2017).

[5] &quot;Amazon Mechanical Turk&quot;, Mturk.com, 2018. [Online]. Available: https://www.mturk.com/.
[Accessed: 29- Sep- 2018].

[6] D. Brabham, &quot;Crowdsourcing as a Model for Problem Solving&quot;, Convergence: The International
Journal of Research into New Media Technologies, vol. 14, no. 1, pp. 75-90, 2008.

[7] RODRIGUES, Filipe; PEREIRA, Francisco; RIBEIRO, Bernardete. Gaussian process classification
and active learning with multiple annotators. En International Conference on Machine Learning. 2014. p.
433-441.

[8] ZHANG, Jing; WU, Xindong; SHENG, Victor S. Imbalanced multiple noisy labeling. IEEE
Transactions on Knowledge and Data Engineering, 2015, vol. 27, no 2, p. 489-503.

[9] RAYKAR, Vikas C., et al. Learning from crowds. Journal of Machine Learning Research, 2010, vol.
11, no Apr, p. 1297-1322.

[10] ZHANG, Jing; WU, Xindong; SHENG, Victor S. Learning from crowdsourced labeled data: a
survey. Artificial Intelligence Review, 2016, vol. 46, no 4, p. 543-576.

[11] GROOT, Perry; BIRLUTIU, Adriana; HESKES, Tom. Learning from multiple annotators with
Gaussian processes. En International Conference on Artificial Neural Networks. Springer, Berlin,
Heidelberg, 2011. p. 159-164.

[12] Yan, Y., Rosales, R., Fung, G., Schmidt, M., Hermosillo, G., Bogoni, L., ... &amp; Dy, J. (2010, March).
Modeling annotator expertise: Learning when everybody knows a bit of something. In Proceedings of the
Thirteenth International Conference on Artificial Intelligence and Statistics (pp. 932-939).

[13] RODRIGUES, Filipe, et al. Learning supervised topic models for classification and regression from
crowds. IEEE transactions on pattern analysis and machine intelligence, 2017, vol. 39, no 12, p. 2409-
2422.

[14] RODRIGUES, Filipe Manuel Pereira Duarte. Probabilistic models for learning from crowdsourced
data. 2016. Tesis Doctoral.
[15] RISTOVSKI, Kosta, et al. Regression Learning with Multiple Noisy Oracles. En ECAI. 2010. p.
445-450.

[16] J. Gil-Gonzalez, A. Alvarez-Meza and A. Orozco-Gutierrez, &quot;Learning from multiple annotators
using kernel alignment&quot;, Pattern Recognition Letters, vol. 116, pp. 150-156, 2018.

[18] &quot;Pattern Recognition and Machine Learning&quot;, Journal of Electronic Imaging, vol. 16, no. 4, p.
049901, 2007. Available: 10.1117/1.2819119 [Accessed 14 January 2019].

[19] Howe, J., 2008. Crowdsourcing: Why the Power of the Crowd is Driving the Future of Business, 1st
Edition. Crown Publishing Group, New York, NY, USA.

[20] M. Esmaeily, H.S. Yazdi, S. Abbassi, R. Monsefi, Hierarchical cooperation of ex-
perts in learning from crowds, in: ICCKE, IEEE, 2016, pp. 211–217.

[21] Little, M. (2019). UCI Machine Learning Repository: Parkinsons Data Set. [online]
Archive.ics.uci.edu. Available at: https://archive.ics.uci.edu/ml/datasets/parkinsons [Accessed 3 Aug.
2019].

[22] Little, M., McSharry, P., Roberts, S., Costello, D. and Moroz, I. (2007). Exploiting Nonlinear
Recurrence and Fractal Scaling Properties for Voice Disorder Detection. Nature Precedings.

[23] H. Wolberg, W. (2019). UCI Machine Learning Repository: Breast Cancer Wisconsin (Diagnostic)
Data Set. [online] Archive.ics.uci.edu. Available at:
https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic) [Accessed 3 Aug. 2019].

[24] Barreto, G. and da Rocha Neto, A. (2019). UCI Machine Learning Repository: Vertebral Column
Data Set. [online] Archive.ics.uci.edu. Available at:
http://archive.ics.uci.edu/ml/datasets/vertebral+column [Accessed 3 Aug. 2019].

[25] Sigillito, V. (2019). UCI Machine Learning Repository: Ionosphere Data Set. [online]
Archive.ics.uci.edu. Available at: https://archive.ics.uci.edu/ml/datasets/ionosphere [Accessed 3 Aug.
2019].

[26] Garcia Maya, A. (2019). FelipeGarcia911/LearningFromCrowds. [online] GitHub. Available at:
https://github.com/FelipeGarcia911/LearningFromCrowds [Accessed 16 Aug. 2019].
