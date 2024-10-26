# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define lzc = Character("吕志聪")
define wlm = Character('王黎明')


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg club

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show sylvie blue normal


    # 此处显示各行对话。

    lzc "              "

    show sylvie blue smile

    lzc "嘿，亲爱的黎明君，今天的课怎么样？"

    show sylvie green normal

    wlm "我。。。挺好的。"

    show sylvie green surprised

    wlm "当然才不会和你说我今天上课只是左耳朵进右耳出啦。"

    show sylvie blue giggle

    lzc '现在要回家了吗，要不要和我一起走？'

    # 此处为游戏结尾。

    return
