# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Map


def test_city_map():
    value = [1]
    attr = ["渝水区"]
    map = Map("新余地图示例", width=1200, height=600)
    map.add("", attr, value, maptype='新余', is_visualmap=True,
            visual_text_color='#000')
    # To avoid potential pinyin crash, all cities have a province prefix
    html = map._repr_html_()
    assert "jiang1_xi1_xin1_yu2" in html
    print(html)
    assert "nbextensions/echarts-china-cities-js" in html
