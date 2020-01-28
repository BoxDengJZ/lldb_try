# lldb_try
感恩 FB 的 chisel, 和 WWDC 相关



<hr>

[blog: 来一点 SB 技巧，lldb 的 Scripting Bridge 框架，新手友好的 Debug 进阶](https://juejin.im/post/5e2de376e51d4558836e3f27)


可以使用 “nege”， 也可以使用 “nudge 修改后” 


<hr>


这样使用 `nege`

```

(lldb) nege 0x104d1ab90
Total offset: (0.0, 0.0)
(CGRect) $17 = (origin = (x = 20, y = 12), size = (width = 51.5, height = 20.5))

// 移动位置
(lldb) nege -c 20 0 0x104d1ab90
Total offset: (20.0, 0.0)
(CGRect) $20 = (origin = (x = 40, y = 12), size = (width = 51.5, height = 20.5))

// 撤销移动位置
(lldb) nege 0x104d1ab90
Total offset: (0.0, 0.0)
(CGRect) $23 = (origin = (x = 20, y = 12), size = (width = 51.5, height = 20.5))

// 移动位置
(lldb) nege -c 20 0 
Total offset: (20.0, 0.0)
(CGRect) $25 = (origin = (x = 40, y = 12), size = (width = 51.5, height = 20.5))

// 撤销移动位置
(lldb) nege 
Total offset: (0.0, 0.0)
(CGRect) $27 = (origin = (x = 20, y = 12), size = (width = 51.5, height = 20.5))
(lldb) 
```

<hr>

# nege 大法三步走

* 进入 lldb

<img src="https://raw.githubusercontent.com/BoxDengJZ/lldb_try/master/imgs/0.png">

* 进入调试界面

<img src="https://raw.githubusercontent.com/BoxDengJZ/lldb_try/master/imgs/1.png">

* 进入 UI 调试界面操作

将 nudge 换成 nege

参数前面 + `-c`

<img src="https://raw.githubusercontent.com/BoxDengJZ/lldb_try/master/imgs/222.png">


<hr>


# UI 全局断点大法。直接取内存。修改当前界面，挺方便的

* 前两步，跟上面的一样，先进入 UI 调试界面

* 进入 UI 调试界面操作

<img src="https://raw.githubusercontent.com/BoxDengJZ/lldb_try/master/imgs/2.png">