print("Hello GitHub!")
print("Hello GitHub!")



```
调用技能 baan-4gl-dataflow-analyzer，读取source目录下全部4GL源码，执行数据流分析。
按照SKILL.md里面的全部规则执行：
1. 全部业务信息从4GL源码读取，不使用外部业务假设。
2. 生成日文データフロー分析報告書，报告内完整保留表、字段、CRUD明细，每条结论标记 CONFIRMED / INFERRED / UNKNOWN。
3. Mermaid流程图使用 graph LR 横向；只绘制核心业务主干，合并临时表、内部微小调用，精简节点，不要把所有数据表全部放进图。
4. 输出2个文件：
output/baan_dataflow_report.md
output/diagrams/flow.mmd
5. 仅读取源码，不修改任何文件，不执行终端命令。
```
