<h1 align="center">_✨ 心灵鸡汤 ✨_</h1>
<p align="center">
<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/Monarchdos/nonebot_plugin_soup.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot_plugin_soup">
    <img src="https://img.shields.io/pypi/v/nonebot_plugin_soup.svg" alt="pypi">
</a>
<a href="https://www.python.org">
    <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
</a>
</p>

## 📖 介绍

来一碗心灵鸡汤吧。

## 💿 安装

**使用 nb-cli 安装**  
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装  

```bash
nb plugin install nonebot-plugin-soup
```

**使用 pip 安装**  
```bash
pip install nonebot-plugin-soup
```

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入
```python
nonebot.load_plugin('nonebot_plugin_soup')
```

**升级插件**  
```bash
pip install --upgrade nonebot-plugin-soup
```

## 🎉 使用

<table> 
  <tr align="center">
    <th> 指令 </th>
    <th> 说明 </th>
  </tr>
  <tr align="center">
    <td> 鸡汤 </td>
    <td> 获取一碗心灵鸡汤 </td>
  </tr>
  <tr align="center">
    <td> 毒鸡汤 </td>
    <td> 获取一碗心灵毒鸡汤 </td>
  </tr>

</table>

## 📃 配置项

直接在全局配置项`env.dev`后添加即可，配置项修改后重启NoneBot生效。

#### 	chickensoup_reply_at

类型：Bool

默认值：True

说明：是否开启机器人回复后艾特用户。

```
 chickensoup_reply_at=true
```

## 📝 更新日志

<details>
<summary>展开/收起</summary>

## **2024-07-15 V1.1.0**

  * 优化代码结构.
  * 新增机器人回复是否'@用户'的设置.

## **2023-01-11 V1.0.0**

  * 插件发布~

</details>
