from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline, Line
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
import random


def r_values():
    return [random.randint(200, 500) for i in range(12)]


def s_values():
    return [random.randint(40, 80) for i in range(12)]


x = Faker.months
tl = Timeline(init_opts=opts.InitOpts(width='1200px', height='700px', page_title='组合图表展示', theme=ThemeType.WESTEROS))
for i in range(2015, 2021):
    bar = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("品牌A规模", r_values(), color='#C43C3C')
        .add_yaxis("品牌B规模", r_values(), color='#5D52A0')
        .extend_axis(
            yaxis=opts.AxisOpts(
                name='收入',
                axislabel_opts=opts.LabelOpts(formatter="{value} 万")
            )
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="两竞争品牌{}年营收与规模情况对比".format(i)),
            yaxis_opts=opts.AxisOpts(name='规模', axislabel_opts=opts.LabelOpts(formatter="{value} 万"), min_=200, max_=500),
            legend_opts=opts.LegendOpts(pos_top='5%'),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
        )
    )

    line = (Line()
            .add_xaxis(x)
            .add_yaxis("品牌A营收", s_values(), yaxis_index=1, color='#C43C3C')
            .add_yaxis('品牌B营收', s_values(), yaxis_index=1, color='#5D52A0')
        )
    bar.overlap(line)
    tl.add(bar, "{}年".format(i))

tl.render("output/multi.html")
