# -*- coding:utf-8 -*-

from pyecharts.charts import Line
from pyecharts import options as opts
from datas import covid_19_data, country_name_map


def _line():
    yaxis_data = [_['value'][0] for _ in covid_19_data]
    xaxis_data = [country_name_map[_['name']] for _ in covid_19_data]
    chart_line = (
        Line()
            .add_xaxis(xaxis_data=xaxis_data)  # data of x label, [str,str,str]
            .add_yaxis(
            series_name="full vaccinated",
            y_axis=yaxis_data,  # data of y label, [num,num,num]
            markpoint_opts=opts.MarkPointOpts(
                data=[  # mark
                    opts.MarkPointItem(type_="min"), opts.MarkPointItem(type_="max")
                ]
            ),
        )
            .set_global_opts(
            # title_opts=opts.TitleOpts(title="Line-MarkPoint"),  # title
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),  # tilt the x label
        )
    )

    return chart_line


chartLine = _line()
chartLine.render("module_result/line.html")
