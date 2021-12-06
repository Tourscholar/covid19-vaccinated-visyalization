# -*- coding:utf-8 -*-

# Max and Min

from pyecharts import options as opts
from pyecharts.charts import Liquid
from pyecharts.commons.utils import JsCode
from datas import covid_19_data, country_name_map

percent_min_data = min([_['value'][0] for _ in covid_19_data])
percent_max_data = max([_['value'][0] for _ in covid_19_data])
vaccinated_min_data = min([_['value'][1] for _ in covid_19_data])
vaccinated_max_data = max([_['value'][1] for _ in covid_19_data])


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


percent_max_, percent_min_ = _liquid()
percent_max_.render('module_result/liquid_1.html')
percent_min_.render('module_result/liquid_2.html')
