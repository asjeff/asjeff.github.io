from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Pie, Tab, WordCloud

src_filename = 'data/龙族一-人物词频.csv'
src_file = open(src_filename, 'r')
line_list = src_file.readlines()
src_file.close()
print(line_list)

wordfre_list = []
for line in line_list:
    line = line.strip()
    split = line.split(',')
    wordfre_list.append((split[0], split[1]))
del wordfre_list[0]


def wordcloud() -> WordCloud:
    c = (
        WordCloud()
        .add('', wordfre_list,
             word_size_range=[20, 80],
             textstyle_opts=opts.TextStyleOpts(font_family='cursive'),
             shape='star')
        .set_global_opts(title_opts=opts.TitleOpts(title='龙族一词频统计——词云图'))
    )
    return c


def bar_datazoom_slider() -> Bar:
    name_list = []
    value_list = []
    for i in wordfre_list:
        name_list.append(i[0])
        value_list.append(i[1])

    c = (
        Bar()
        .add_xaxis(name_list)
        .add_yaxis("龙族一", value_list)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="龙族一词频统计——柱状图"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


def pie_rosetype() -> Pie:
    name_list = []
    value_list = []
    for i in wordfre_list:
        name_list.append(i[0])
        value_list.append(i[1])
    c = (
        Pie()
        .add(
            "",
            wordfre_list[0:20],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add(
            "",
            wordfre_list[0:20],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="area",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="龙族一词频统计——玫瑰图"),
                         legend_opts=opts.LegendOpts(type_='scroll', pos_top='5%'))
    )
    return c


out_filename = 'output/frequency.html'
tab = Tab(page_title='词频统计可视化')
tab.add(wordcloud(), '词云图')
tab.add(bar_datazoom_slider(), "柱状图")
tab.add(pie_rosetype(), "玫瑰图")
tab.render(out_filename)
