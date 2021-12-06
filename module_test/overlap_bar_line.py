# -*- coding:utf-8 -*-

from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.faker import Faker
from datas import covid_19_data_, country_name_map,covid_19_data

percent_min_data = min([_['value'][0] for _ in covid_19_data])
percent_max_data = max([_['value'][0] for _ in covid_19_data])
vaccinated_min_data = min([_['value'][1] for _ in covid_19_data])
vaccinated_max_data = max([_['value'][1] for _ in covid_19_data])

xaxis_data = [country_name_map[_['name']] for _ in covid_19_data_]
yaxis_one_data = [_['value'][0] for _ in covid_19_data_]
yaxis_two_data = [round(_['value'][1] / 10000, 2) for _ in covid_19_data_]


def _overlap():
    xaxis_data = [country_name_map[_['name']] for _ in covid_19_data_]
    yaxis_one_data = [_['value'][0] for _ in covid_19_data_]
    yaxis_two_data = [round(_['value'][1] / 10000, 2) for _ in covid_19_data_]
    chart_overlap = (
        Bar()
            .add_xaxis(xaxis_data)
            .add_yaxis(
            series_name="ten thousand/만",
            y_axis=yaxis_two_data,
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} %"), interval=5,
            )
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} 만"),
            ),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),  # tilt the x label
        )
    )
    #
    line = (
        Line()
            .add_xaxis(xaxis_data=xaxis_data)
            .add_yaxis(
            series_name="%",
            y_axis=yaxis_one_data,
            yaxis_index=1,
            markpoint_opts=opts.MarkPointOpts(
                data=[  # mark
                    opts.MarkPointItem(type_="min"), opts.MarkPointItem(type_="max"),
                ]
            )
        )
    )
    chart_overlap.overlap(line)
    return chart_overlap


chartOverlap = _overlap()
chartOverlap.render("module_result/overlap_bar_line.html")
