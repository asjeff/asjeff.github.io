from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

data = {
    "广东": 110761,
    "山东": 71067,
    "河南": 54997,
    "四川": 48599,
    "江苏": 102719,
    "河北": 36207,
    "湖南": 41781,
    "安徽": 38681,
    "湖北": 43443,
    "浙江": 64613,
    "广西": 22157,
    "云南": 24500,
    "江西": 25692,
    "辽宁": 25115,
    "福建": 43904,
    "陕西": 26181,
    "黑龙江": 13698,
    "山西": 17652,
    "贵州": 17827,
    "重庆": 25003,
    "吉林": 12311,
    "甘肃": 9017,
    "内蒙古": 17360,
    "新疆": 13798,
    "上海": 38701,
    "台湾": 45855,
    "北京": 36103,
    "天津": 14084,
    "海南": 5532,
    "香港": 24104,
    "宁夏": 3921,
    "青海": 3006,
    "西藏": 1903,
    "澳门": 1579,
}
map_data = list(data.items())
c = (
    Map(init_opts=opts.InitOpts(width='1000px', height='700px', page_title='中国地图'))
    .add("各省GDP总量", map_data, maptype="china",
         is_map_symbol_show=False)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2020年全国各省GDP总量图", subtitle='GDP单位：亿元'),
        visualmap_opts=opts.VisualMapOpts(max_=115000, min_=1900, is_piecewise=True,
                                          range_color=["lightskyblue", "yellow", "orangered"]),
        legend_opts=opts.LegendOpts(pos_top="5%")
    )
    .render("output/china_map.html")
)
