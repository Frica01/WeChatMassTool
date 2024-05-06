<div align="center" height="256" width="256">
    <h1 style="font-size:36pt; font-weight:600; color:#ff79c6;">WeChatMassTool</h1>
<br>
<img alt="Python 3.12.0" src="https://img.shields.io/badge/Python-3.12.0-informational?style=flat&logo=python&logoColor=white&color=3776AB"/>
<img alt="PySide6" src="https://img.shields.io/badge/PySide6-Compatible-informational?style=flat&logo=qt&logoColor=white&color=41CD52"/>
<img alt="PyQt6" src="https://img.shields.io/badge/PyQt6-Compatible-informational?style=flat&logo=qt&logoColor=white&color=41CD52"/>
<img alt="License" src="https://img.shields.io/badge/license-MIT-green?style=flat&logo=opensourceinitiative&logoColor=white"/>

</div>

# ΢��Ⱥ������

## ?Ŀ¼
- [��Ŀ���](#��Ŀ���)
- [��������](#��������)
- [��ͼչʾ](#��ͼչʾ)
- [֧����Ŀ](#֧����Ŀ)
- [����](#����)
- [��Ŀ�ṹ](#��Ŀ�ṹ)
- [��չ](#��չ)
- [��ϵ����](#��ϵ����)
- [����](#����)
- [���֤](#���֤)

## ?��Ŀ���
΢��Ⱥ��������һ������ `PySide6` �� `Python` ����������Ӧ�ó���ּ�ڰ����û���Ч��ִ��΢����Ϣ��Ⱥ���������ṩ��һ���Ѻõ��û����棬֧�ֵ���Ⱥ�������͵������н����

## ?��������
>����Ŀʹ�� `Python` �� `PySide6`��ȷ�����Ѿ���װ�� `Python 3.12+` �� `PySide6`

<br>

1. ��¡�ֿ⵽����
   ```bash
   git clone https://github.com/Frica01/PinnacleQt_GUI_PySide6_PyQt6.git
   ```
<br>

2. ��װ��������
   ```bash
   pip install -r requirements.txt
   ```
<br>

3. ����Ӧ��
   ```bash
   python main.py
   ```

## ?��ͼչʾ

<details>
<summary><b>չ��</b></summary>


### ��������

<img src="assets/program_launch.gif" alt="program_launch"/>

### ����չʾ

<img src="assets/program_animation.gif" alt="assets%2Fprogram_animation"/>

### ����չʾ

<img src="assets/program_running.gif" alt="assets%program_running"/>



</details>

## ?֧����Ŀ

��������������Ŀ���ã���������һ��??��`Star`����`Star`������˵��һ�ֹ�����Ҳ�ܰ�������Ŀ����߷���������ߡ�

�����ϣ���������µĸ��º͸Ľ�����`Fork`?����Ŀ��`Fork`�����������ֶ���Ŀ���µ�ͬ�������л��ṱ���Լ��ĸĽ����¹��ܡ�

## ����
<font size=6 color=Violet>��Ҫ˵����</font>
- **���� MVC �ܹ�**��ͨ��ģ�ͣ�Model������ͼ��View���Ϳ�������Controller���ķ��룬ʵ�����߼������Ľ��Ϊ��Ŀ�ĺ���ά������չ�����˼�ʵ������
- **������չ**��MVC�ܹ����������¹��ܱ�ø������׺�ֱ�ӣ������޸Ĵ������д��뼴��ʵ�ֹ��ܵ���չ��
- **���ܳ���**������Ŀ�еĳ��ù��ܺ��������ɶ�����ģ��ͺ���������˴���ĸ����ԣ�ͬʱҲ���˹��ܵ��޸ĺ��������̡�


<font color='bluesky' size=6>�ѿ�����</font>
-[x] **�û��ѺõĽ���**������ `PySide6`��ӵ���ִ����Ľ�����������û����顣
-[x] **����Ⱥ��**�����Ը����û����õı�ǩ��Ⱥ���������Ⱥ����
-[x] **�ḻ����Ϣ����**��֧���ı���ͼƬ���ļ��ȶ������͵���Ϣ���ݡ�
-[x] **��־��¼**����ϸ��¼ÿ�η��͵Ľ���������û��ز顣

<font color='red' size=6>��������</font>
-[ ] **��Ϣģ��**�����Ӹ����Զ�����Ϣģ�塣
-[ ] **��Ϣ��ʱ**����Ϣ�Ķ�ʱ���͹��ܡ�

## ��Ŀ�ṹ

<details>
<summary><b>չ��</b></summary>

```md
WeChatMassTool/
������ assets/              # չʾͼƬ
������ config/              # Ӧ����������ļ�
��   ������ __init__.py
��   ������ config.py        # Ӧ�õ�ȫ����������
������ controllers/         # MVC �еĿ��������
��   ������ __init__.py
��   ������ controller_main.py
������ make/                # pyinstaller����ļ�
������ models/              # MVC �е�ģ����������������߼�
��   ������ __init__.py
��   ������ model_generator_csv.py
��   ������ model_main.py
������ tests/               # ��Ԫ���Ժ͹��ܲ����ļ�
��   ������ __init__.py
��   ������ test.py
������ utils/
��   ������ __init__.py
��   ������ utils.py
��   ������ wx_operation.py
��   ������ wx_operation.py.bak
������ views/               # MVC �е���ͼ������û������ļ�
��   ������ resources/       # UI ��Դ����ͼ�ꡢͼƬ��
��   ��   ������ icons/
��   ��   ������ images/
��   ��   ������ svgs/
��   ��   ������ themes/      # UI �����ļ�
��   ��   ������ ui_files/    # Qt Designer UI �ļ�
��   ��   ������ resources.qrc
��   ������ ui_components/   # ���õ�UI������߼�
��   ��   ������ __init__.py
��   ��   ������ animations.py  # ����Ч��ʵ��
��   ��   ������ ui_setup.py    # UI���úͳ�ʼ��
��   ������ ui_designs/      # UI ����ļ�������PySide6�Զ����ɵ�Python�ļ�
��   ��   ������ __init__.py
��   ��   ������ resources_rc.py
��   ��   ������ ui_login.py    # ��¼����UI���
��   ��   ������ ui_main.py     # ������UI���
��   ������ widgets/         # �Զ����Qt Widgets
��   ��   ������ __init__.py
��   ��   ������ custom_grips.py  # �Զ��崰�ڵ�����С�ؼ�
��   ��   ������ login_window.py  # ��¼����ʵ��
��   ��   ������ main_window.py   # ������ʵ��
��   ������ __init__.py
��   ������ view_main.py     # ����ͼ���������������Ϻ͹���Ӧ�õ�������ͼ
������ LICENSE
������ README.md
������ main.py              # Ӧ�ó��������ļ�
������ requirements.txt

```
</details>

## ��չ
����ĿĿǰ֧�ֻ�����Ⱥ�����ܣ�δ���İ汾�ƻ�������
- ���Ӹ����Զ�����Ϣģ�塣
- �û���Ϊ������ʹ�÷������ܣ����ڸ���Ӧ�����ܺ��û����顣

## ??��ϵ����
��������κ����������Ҫ������˽���Ŀ����ӭͨ�����·�ʽ��ϵ�ң�
- ΢�Ź��ںţ�С�˵�Python�ӻ��� [ɨ���ע���ں�](./assets/WeChat_Official_Account.jpg)
- QQȺ�ģ�[ɨ�����Ⱥ��](./assets/QQ_group.png)
- ��GitHub�� [�ύIssue](https://github.com/Frica01/WeChatMassTool/issues)

## ����
����Ŀ�������Դ�� [**Frica01**](https://github.com/Frica01) �Ĵ���͹��ף��Ҷ����ڿ�Դ�����Ĺ�����ʾ���Եľ��Ժ͸�л������Ŀ��������������Ŀ���ع���
- [https://github.com/Frica01/WeChat-mass-msg](https://github.com/Frica01/WeChat-mass-msg)
- [https://github.com/Frica01/PinnacleQt_GUI_PySide6_PyQt6](https://github.com/Frica01/PinnacleQt_GUI_PySide6_PyQt6)


��ӭ����Ŀ����Ȥ�Ŀ�����ͨ�� [Pull Requests](https://github.com/Frica01/WeChatMassTool/pulls) �� [Issues](https://github.com/Frica01/WeChatMassTool/issues) �ύ���Ĺ��׻�����

## ���֤
����Ŀ�� MIT ���֤�¿�Դ��������������� GitHub �ֿ��� [LICENSE](LICENSE) �ļ���
