关系计数软件

### 类名：RelationDefineByMatrix

#####  变量：矩阵m

| 函数名           | 功能                         | 输出                         |
| :--------------- | ---------------------------- | ---------------------------- |
| matrix2num       | 将布尔矩阵转成二进制数       | 二进制数（以字符串形式输出） |
| QReflexitive     | 判断关系矩阵是否具有自反性   | true/false                   |
| QAntiReflexitive | 判断关系矩阵是否具有反自反性 | true/false                   |
| QSymmetric       | 判断关系矩阵是否具有对称性   | true/false                   |
| QAntiSymmetric   | 判断关系矩阵是否具有反对称性 | true/false                   |
| QTransitive      | 判断关系矩阵是否具有传递性   | true/false                   |

### 类名：RelationDefineByInt

#####  变量：十进制数 n；集合元素个数 size

| 函数名           | 功能                               | 输出                 |
| :--------------- | ---------------------------------- | -------------------- |
| num2matrix       | 将十进制数转成布尔矩阵（关系矩阵） | 关系矩阵（np.array） |
| QReflexitive     | 判断该关系是否具有自反性           | true/false           |
| QAntiReflexitive | 判断该关系是否具有反自反性         | true/false           |
| QSymmetric       | 判断该关系是否具有对称性           | true/false           |
| QAntiSymmetric   | 判断该关系是否具有反对称性         | true/false           |
| QTransitive      | 判断该关系是否具有传递性           | true/false           |

### 类名：RelationComb

#####  变量：集合元素个数 size

| 函数名                                             | 功能                                                         | 输出                             |
| -------------------------------------------------- | ------------------------------------------------------------ | -------------------------------- |
| CRelations                                         | 计算size个元素的集合上关系的总数                             | 十进制数                         |
| generate_all_relations                             | 计算size个元素的集合上的所有关系的二进制表示                 | 二进制数（以字符串形式输出）list |
| generate_relation_matrix                           | 计算size个元素的集合上的所有关系的布尔矩阵表示               | 关系矩阵list                     |
| CReflexiviteRelations                              | 计算size个元素的集合上自反关系的总数                         | 十进制数                         |
| generate_all_reflexive_relations                   | 计算size个元素的集合上的自反关系的二进制表示                 | 二进制数（以字符串形式输出）list |
| generate_reflexive_relation_matrix                 | 计算size个元素的集合上的自反关系的布尔矩阵表示               | 关系矩阵list                     |
| CAntireflexiviteRelations                          | 计算size个元素的集合上反自反关系的总数                       | 十进制数                         |
| generate_all_antireflexivite_relations             | 计算size个元素的集合上的反自反关系的二进制表示               | 二进制数（以字符串形式输出）list |
| generate_antireflexivite_relation_matrix           | 计算size个元素的集合上的反自反关系的布尔矩阵表示             | 关系矩阵list                     |
| CSymmetricRelations                                | 计算size个元素的集合上对称关系的总数                         | 十进制数                         |
| generate_all_symmetric_relations                   | 计算size个元素的集合上的对称关系的二进制表示                 | 二进制数（以字符串形式输出）list |
| generate_symmetric_relation_matrix                 | 计算size个元素的集合上的对称关系的布尔矩阵表示               | 关系矩阵list                     |
| CAntisymmetricRelations                            | 计算size个元素的集合上反对称关系的总数                       | 十进制数                         |
| generate_all_antisymmetric_relations               | 计算size个元素的集合上的反对称关系的二进制表示               | 二进制数（以字符串形式输出）list |
| generate_antisymmetric_relation_matrix             | 计算size个元素的集合上的反对称关系的布尔矩阵表示             | 关系矩阵list                     |
| CReflexiviteSymmetricRelations                     | 计算size个元素的集合上自反且对称关系的总数                   | 十进制数                         |
| generate_all_reflexivite_symmetric_relations       | 计算size个元素的集合上的自反且对称的关系的二进制表示         | 二进制数（以字符串形式输出）list |
| generate_reflexivite_symmetric_relation_matrix     | 计算size个元素的集合上的自反且对称的关系的布尔矩阵表示       | 关系矩阵list                     |
| CAntireflexiviteSymmetricRelations                 | 计算size个元素的集合上反自反且对称关系的总数                 | 十进制数                         |
| generate_all_antireflexivite_symmetric_relations   | 计算size个元素的集合上的反自反且对称的关系的二进制表示       | 二进制数（以字符串形式输出）list |
| generate_antireflexivite_symmetric_relation_matrix | 计算size个元素的集合上的反自反且对称的关系的布尔矩阵表示     | 关系矩阵list                     |
| CNotReRelations                                    | 计算size个元素的集合上既不自反也不反自反的总数               | 十进制数                         |
| generate_all_notre_relations                       | 计算size个元素的集合上的既不自反也不反自反的关系的二进制表示 | 二进制数（以字符串形式输出）list |
| generate_notre_relation_matrix                     | 计算size个元素的集合上的既不自反也不反自反的关系的布尔矩阵表示 | 关系矩阵list                     |
| CNotReSymmetricRelations                           | 计算size个元素的集合上既不自反也不反自反的对称关系的总数     | 十进制数                         |
| generate_all_notre_symmetric_relations             | 计算size个元素的集合上的既不自反也不反自反的对称关系的二进制表示 | 二进制数（以字符串形式输出）list |
| generate_notre_symmetric_relation_matrix           | 计算size个元素的集合上的既不自反也不反自反的对称关系的布尔矩阵表示 | 关系矩阵list                     |
| CTransitive                                        | 计算size个元素的集合上传递关系的总数                         | 十进制数                         |
| generate_all_transitive_relations                  | 计算size个元素的集合上的传递关系的二进制表示                 | 二进制数（以字符串形式输出）list |
| generate_transitive_relation_matrix                | 计算size个元素的集合上的传递关系的布尔矩阵表示               | 关系矩阵list                     |
| CPartialOrder                                      | 计算size个元素的集合上偏序关系的总数                         | 十进制数                         |
| generate_all_partialOrder_relations                | 计算size个元素的集合上的偏序关系的二进制表示                 | 二进制数（以字符串形式输出）list |
| generate_partialOrder_relation_matrix              | 计算size个元素的集合上的偏序关系的布尔矩阵表示               | 关系矩阵list                     |
| CQuasiOrder                                        | 计算size个元素的集合上拟序关系的总数                         | 十进制数                         |
| generate_all_quasiOdering_relations                | 计算size个元素的集合上的拟序关系的二进制表示                 | 二进制数（以字符串形式输出）list |
| generate_quasiOdering_relation_matrix              | 计算size个元素的集合上的拟序关系的布尔矩阵表示               | 关系矩阵list                     |

