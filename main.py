
import lizard as lz
import argparse
import sys

# lizard.auto_open('target.cpp')
# r = lizard.analyze('.')
# for n in r:
#     print(n)
analyze_file = lz.FileAnalyzer(lz.get_extensions([]))  # pylint: disable=C0103


def main(argv=None):
    """Command-line entrance to Lizard.

    Args:
        argv: Arguments vector; if None, sys.argv by default.
    """
    options = lz.parse_args(argv or sys.argv)
    printer = options.printer or lz.print_result
    schema = lz.OutputScheme(options.extensions)
    if schema.any_silent():
        printer = lz.silent_printer
    schema.patch_for_extensions()
    if options.input_file:
        options.paths = lz.auto_read(options.input_file).splitlines()
    original_stdout = sys.stdout
    output_file = None
    if options.output_file:
        output_file = lz.open_output_file(options.output_file)
        sys.stdout = output_file
    result = lz.analyze(
        options.paths,
        options.exclude,
        options.working_threads,
        options.extensions,
        options.languages)
    warning_count = printer(result, options, schema, lz.AllResult)
    lz.print_extension_results(options.extensions)
    list(result)
    if output_file:
        sys.stdout = original_stdout
        output_file.close()
    if 0 <= options.number < warning_count:
        sys.exit(1)


main()
# def show

# import pandas as pd
# import pymap3d as pm
# import folium

# nagoya_lat = 35.181568
# nagoya_lon = 136.906778
# nagoya = [35.181568, 136.906778]

# osaka_lat = 34.693737
# osaka_lon = 135.502167
# osaka = [osaka_lat, osaka_lon]

# tokyo_lat =  35.689543
# tokyo_lon = 139.692011
# tokyo = [tokyo_lat, tokyo_lon]


# def get_map():

#     m = folium.Map(location=[nagoya_lat,nagoya_lon],zoom_start=10)
#     folium.Marker(location=[nagoya_lat, nagoya_lon], popup=folium.Popup("名古屋市役所",show=True)).add_to(m)
#     folium.Marker(location=[osaka_lat, osaka_lon], popup=folium.Popup("大阪市役所",show=True)).add_to(m)
#     folium.Marker(location=[tokyo_lat, tokyo_lon], popup=folium.Popup("東京都庁",show=True)).add_to(m)

#     folium.PolyLine(locations=[nagoya, osaka]).add_to(m)
#     folium.PolyLine(locations=[nagoya, tokyo]).add_to(m)

#     return m

# def get_df():
#     df = pd.DataFrame()
#     df['name'] = ['名古屋市役所', '大阪市役所', '東京都庁']
#     df['lat'] = [nagoya_lat, osaka_lat, tokyo_lat]
#     df['lon'] = [nagoya_lon, osaka_lon, tokyo_lon]
#     return df
