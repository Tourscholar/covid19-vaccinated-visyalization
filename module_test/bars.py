# -*- coding:utf-8 -*-

from pyecharts.charts import Bar
from pyecharts import options as opts
from datas import covid_19_data, country_name_map

percent_min_data = min([_['value'][0] for _ in covid_19_data])
percent_max_data = max([_['value'][0] for _ in covid_19_data])
vaccinated_min_data = min([_['value'][1] for _ in covid_19_data])
vaccinated_max_data = max([_['value'][1] for _ in covid_19_data])


def _bar():
    xaxis_data = [country_name_map[_['name']] for _ in covid_19_data][::-1]
    yaxis_data = [round(_['value'][1] / 10000, 2) for _ in covid_19_data][::-1]
    chart_bar = (
        Bar()
            .add_xaxis(xaxis_data)  # data of incoming x-axis, [1,2,3,4,5]
            .add_yaxis(
            series_name="",  
            y_axis=yaxis_data,  # data of y axis, [num,num,num]
            label_opts=opts.LabelOpts(  # label configuration
                position='right',  # displayed of label，inside，left，top，bottom
                formatter="{b}: {c}만"  # display format of label
            )
        )
            .reversal_axis()  # x-axis and y-axis upside down
            .set_global_opts(
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),  # do not display the labels of the axis
            tooltip_opts=opts.TooltipOpts(is_show=False),  # turn off touch display
            visualmap_opts=opts.VisualMapOpts(
                dimension=0,
                range_text=['Max', 'Min'], 
                # is_calculable=True,  
                # range_color=["lightskyblue", "red", "pink"],  # color
                # textstyle_opts=opts.TextStyleOpts(
                #     color="rgba(0,0,0,0.5)"  # text color
                # ),
                min_=round(vaccinated_min_data / 10000, 2),  # Min
                max_=round(vaccinated_max_data / 10000, 2),  # Max
            )
        )
    )
    return chart_bar


chart_bar = _bar()
chart_bar.render("module_result/bar.html")
