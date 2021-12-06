# -*- coding:utf-8 -*-

from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from datas import covid_19_data, country_name_map

percent_min_data = min([_['value'][0] for _ in covid_19_data])
percent_max_data = max([_['value'][0] for _ in covid_19_data])
vaccinated_min_data = min([_['value'][1] for _ in covid_19_data])
vaccinated_max_data = max([_['value'][1] for _ in covid_19_data])


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


chartMap = _map()
chartMap.render("module_result/map.html")
