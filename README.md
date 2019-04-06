README
===========================
****
#[交流学习](https://jq.qq.com/?_wv=1027&k=56mqERV "QQ群"):blush:
****
# Symbols The following characters have a geometric interpretation.
|#|Character |Meaning|
|---|----|-----|
|1|`F`| Move forward by line length drawing a line|
|2|`f `|Move forward by line length without drawing a line|
|3|`+`|Turn left by turning angle|
|4|`-`|Turn right by turning angle|
|5|/|Reverse direction (ie: turn by 180 degrees)|
|6|`[`|Push current drawing state onto stack|
|7|`]`|Pop current drawing state from the stack|
|8|`#`|Increment the line width by line width increment|
|9|`!`| Decrement the line width by line width increment|
|10|`@`| Draw a dot with line width radius|
|11|`{`|Open a polygon|
|12|`}`|Close a polygon and fill it with fill colour|
|13|`<`| Multiply the line length by the line length scale factor|
|14|`>`|Divide the line length by the line length scale factor|
|15|`&`|Swap the meaning of + and -|
|16|`(`|Decrement turning angle by turning angle increment|
|17|`)`|Increment turning angle by turning angle increment|
****
# 以下符号字符的几何解释。
|#|字符 |含义|
|---|----|-----|
|1|`F`|按行绘制一条线向前移动|
|2|`f `|按线条长度向前移动而不绘制线条|
|3|`+`|通过转动角度向左转动|
|4|`-`|通过转动角度向右转动|
|5|/|反向（即：转动180度）|
|6|`[`|将当前绘图状态推入堆栈|
|7|`]`|从堆栈弹出当前绘图状态|
|8|`#`|按线宽增量增加线宽|
|9|`!`| 通过线宽增量减小线宽|
|10|`@`| 绘制带有线宽半径的点
|12|`}`|关闭多边形并用填充颜色填充
|13|`<`| 将线长乘以线长比例因子|
|14|`>`|将线长除以线长比例因子|
|15|`&`|交换+和 - 的含义|
|16|`(`|通过转动角度增量减小转动角度|
|17|`)`|通过转动角度增量来增加转动角度 |
|18|`{`|打开多边形|
	  
****
# 功能介绍
* draw_path(length, angle, path, expalnation)
    * 主要用来绘制海龟行走路径
        * length ---->每次行走的距离
        * angle  ---->偏移的角度
        * path  ---->初始路径图案,即0阶的形状
        * expalnation  ---->用来记录打印每一步操作
* apply_rules(path, rules)
    * 主要是转换每一阶段的path
        * path  ---->初始路径图案,即0阶的形状
        * rules ---->转换的规则
* getColor()
    * 提供一个随机rgb值
* initialization()
    * 初始化各种参数
* Introduction(x=-600, y=-350)
    * 注解
        * 默认海龟初始位置(-600,-350)
* run(n,angle,length,path,rules)
    * 启动程序