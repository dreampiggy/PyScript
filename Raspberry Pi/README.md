# 树莓派

## 元件

+ 按钮 x3（红黄绿各一个）
+ LED灯 x3（红黄绿各一个）
+ 电阻 300Ω x3, 500Ω x3
+ 三色四针脚LED x1
+ 无源蜂鸣器 x1
+ 杜邦线 若干

## Build

推荐使用原版`Respbian OS`，第三方Linux for ARM7也可以（比如`OSMC`）

```bash
sudo apt-get install python-pip
sudo pip install rpi.gpio
cd Raspberry\ pi/
sudo python reaction.py
```

## 连线

参考图片：
![](http://img.hb.aicdn.com/f12a9b776c228841f2e22ec41e6f957895112f801da557-XIHfVv_fw658)

## 注意

连接元件，对应GPIO端口可以在脚本前10行修改