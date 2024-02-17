REM CNAME:域名配置，github会将主页指向该文件指向的域名
copy .\setList\CNAME .\docs\

REM 网站默认加载图标
copy .\assets\img\favicon.ico .\docs\

REM  各文档引用的图片文件
mkdir .\docs\assets\img
copy .\assets\img\* .\docs\assets\img\

REM 移动profile
mkdir .\docs\assets\img\profile
copy .\assets\img\profile\* .\docs\assets\img\profile

REM 各个文档引用的视频文件
REM mkdir .\docs\assets\video
REM copy .\assets\video\* .\docs\assets\video\

REM 移动theme中的js文件夹及文件到目标文件夹
mkdir .\docs\themes\js
copy .\themes\inUse\js\* .\docs\themes\js\

