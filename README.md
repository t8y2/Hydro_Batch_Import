# Hydro_Batch_Import
本脚本目前只适用于Edge浏览
如果需要在其他版本上运行，只需更改相应驱动即可
本处不作过多阐述

从SYZOJ批量导入题目进Hydro搭建的OJ自动化脚本

#### 版本说明
一共有两个版本
分别是有头【Header_batch.py】和无头【Headless_batch.py】

有头版本即可以看到浏览器的操作运行，能够看到画面
<br>
无头版本即只可以在控制台看到操作信息，因为中间减少了浏览器渲染等过程，效率相对较高。

此处建议使用无头版本

#### 环境配置
在使用前，
请先使用“pip install selenium”命令安装库
另外需要去官网下载相对应的Edge版本包和配置环境变量
可以参考[此处](https://blog.csdn.net/tk1023/article/details/109078613?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164257747016780255212244%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=164257747016780255212244&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-109078613.pc_search_result_cache&utm_term=selenium+edge&spm=1018.2226.3001.4187)

#### 使用说明
<img src="https://pic.imgdb.cn/item/61e7f14f2ab3f51d913fdff6.jpg">
<img src="https://pic.imgdb.cn/item/61e7f02d2ab3f51d913edd47.jpg">
需更改源码中如上图的OJURL,uname和passwd(OJ的SU账号)

