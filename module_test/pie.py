# -*- coding:utf-8 -*-


from pyecharts.charts import Pie
from pyecharts import options as opts
from datas import covid_19_data, country_name_map


def _pie():
    data = [(country_name_map[_['name']], _['value'][0]) for _ in covid_19_data]
    chart_pie = (
        Pie()
            .add(
            series_name="",
            data_pair=data,  # [(key1, value1), (key2, value2)]
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",  # percentage of sector center angle showing data
            label_opts=opts.LabelOpts(is_show=True),
        )
            .set_global_opts(
            # title_opts=opts.TitleOpts(title="Vaccinated Rose"),
            legend_opts=opts.LegendOpts(is_show=False)
        )
    )
    return chart_pie


chartPie = _pie()
chartPie.render("module_result/pie.html")