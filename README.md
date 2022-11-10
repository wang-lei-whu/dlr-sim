<!--
 * @Author: wanglei
 * @Date: 2022-11-03 15:59:29
 * @LastEditTime: 2022-11-10 20:31:55
 * @Description: readme
-->
# dlr-sim
some codes used for simulating DLR model combustion chamber with FLUENT

## input 编码表
|编号|意义|变化范围|
|:-:|:-:|:-:|
|0|air flow|0.01762 10%|
|1|fuel flow|0.000696 10%|
|2|inlet temperature|330K 0-300K|

## output编码表
|编号|意义|变化范围|
|:-:|:-:|:-:|
|0|out-co2|0.105|
|1|out-tem|1800|

## pbs 脚本模式表
0：清理生成文件
1：进行变量输入
2：进行fluent运算
3：进行cfdpost绘图
4：进行python后处理
-h:显示帮助
空：执行全流程
