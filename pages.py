# -*- coding:utf-8 -*-
# author   : SunriseCai
# datetime : 2021-04-11 14:49
# software : PyCharm

from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Pie, Bar, Map, Line, Liquid, Page

from datas import covid_19_data, covid_19_data_, country_name_map

percent_min_data = min([_['value'][0] for _ in covid_19_data])
percent_max_data = max([_['value'][0] for _ in covid_19_data])
vaccinated_min_data = min([_['value'][1] for _ in covid_19_data])
vaccinated_max_data = max([_['value'][1] for _ in covid_19_data])


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

def _map():
    data = [[_['name'], [_['value'][0], round(_['value'][1] / 10000, 2), country_name_map[_['name']]]] for _ in
            covid_19_data]
    chart_map = (
        Map()
            .add(
            series_name='',
            data_pair=data,  # [['country', value],['country', value]]
            maptype='world',
            is_map_symbol_show=False,  
            label_opts=opts.LabelOpts(is_show=False),  
            itemstyle_opts={  
                "normal": {
                    # display
                    "areaColor": "#CED8F6",
                    "borderColor": "#404a59"
                },
                "emphasis": {
                    # touch display
                    "lable": {"show": Map},
                    "areaColor": "rgba(255,255,255, 0.5)"

                },
            }
        )
            .set_global_opts(
            # title
            title_opts=opts.TitleOpts(
                title="Covid-19 World vaccinated 2021-12-06",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=35,
                    color="rgba(155,155,155,0.9)"
                )
            ),
            # top bar
            tooltip_opts=opts.TooltipOpts(
                # formatter="{b}:{c}{d}",  # the style displayed after selection
                # is_show=False
                formatter=JsCode(
                    """
                    function (params){
                      if('value' in params.data){
                          return params.data.value[2] + ' : ' + params.data.value[0] + '% : ' + params.data.value[1]+'만'
                      }
                    }
                    """
                )
            ),
            visualmap_opts=opts.VisualMapOpts(
                # orient='vertical',  
                # is_calculable=True, 
                dimension=0,  
                pos_right='right',  # location
                pos_bottom='bottom',  # location
                range_text=['max', 'min'],  # text at both ends
                # range_color=["lightskyblue", "yellow", "orangered"],  # color
                min_=percent_min_data,  # Min
                max_=percent_max_data,  # Max
            )
        )
    )

    return chart_map


def _liquid():
    percent_max = (
        Liquid()
            .add(
            series_name="Highest ratio",
            data=[round(percent_max_data / 100, 2), 0.3],
            center=["25%", "25%"],
            color='white',
            background_color='lightskyblue',
            is_outline_show=False,  # border
            label_opts=opts.LabelOpts(color='pink', position="inside")
        )
    )
    percent_min = (
        Liquid()
            .add(
            series_name="Minimum ratio",
            data=[percent_min_data / 100, 0.3],
            center=["25%", "25%"],
            is_outline_show=False
        )
    )

    return percent_max, percent_min

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

def _overlap():
    xaxis_data = [country_name_map[_['name']] for _ in covid_19_data_]
    yaxis_one_data = [_['value'][0] for _ in covid_19_data_]
    yaxis_two_data = [round(_['value'][1] / 10000, 2) for _ in covid_19_data_]
    chart_overlap = (
        Bar()
            .add_xaxis(xaxis_data)
            .add_yaxis(
            series_name="Ten thousand/만",
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



def first_run():
    chartBar = _bar()
    chartMap = _map()
    chartLiquid_1, chartLiquid_2 = _liquid()
    chartPie = _pie()
    chartOverlap = _overlap()
    #
    page = Page(page_title="Covid-19 World vaccinated", layout=Page.DraggablePageLayout)
    page.add(chartBar, chartMap, chartLiquid_1, chartLiquid_2, chartPie, chartOverlap)
    page.render('result/render.html')


def second_run():
    Page.save_resize_html(source='result/render.html', cfg_file="./chart_config.json", dest="result/result_.html")


if __name__ == '__main__':
    first_run()
    second_run()
