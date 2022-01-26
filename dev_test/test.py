######
# In this script I have the proxy response with up to 300 lines of orderbook
# I need to create the async loop that will receive this data every few miliseconds
#####


import json


exchange_spec_dict = json.load(open("../admin_tools/exchanges"))

print(exchange_spec_dict)


#
#
# data = json.load(open('../admin_tools/exchanges'))
#
# print(data['currency_mapping']['symbols']['btcpln'])
#
# print(data['source']['rest_url'])

#
# class Periodic:
#     def __init__(self, func, time):
#         self.func = func
#         self.time = time
#         self.is_started = False
#         self._task = None
#
#     async def start(self):
#         if not self.is_started:
#             self.is_started = True
#             # Start task to call func periodically:
#             self._task = asyncio.ensure_future(self._run())
#
#     async def stop(self):
#         if self.is_started:
#             self.is_started = False
#             # Stop task and await it stopped:
#             self._task.cancel()
#             with suppress(asyncio.CancelledError):
#                 await self._task
#
#     async def _run(self):
#         while True:
#             await asyncio.sleep(self.time)
#             self.func()
#
# async def main():
#     p = Periodic(lambda: print('test'), 1)
#     try:
#         print('Start')
#         await p.start()
#         await asyncio.sleep(3.1)
#
#         print('Stop')
#         await p.stop()
#         await asyncio.sleep(3.1)
#
#     finally:
#         await p.stop()  # we should stop task finally
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())

# a = ['asdasd', 'afbdfgbnfg']
#
# print(a['afbdfgbnfg'])


bitkub_url = [{
    'error': 0, 'result': [
        [99545967, 1642788419, 35581.36, 1294200.07, 0.02749294],
        [99545968, 1642788419, 117523.49, 1294200.07, 0.09080783],
        [99545970, 1642788420, 2269059.93, 1294200.07, 1.75325283],
        [99545973, 1642788420, 873774, 1294200.07, 0.675146],
        [99545960, 1642788417, 123025.42, 1294200.06, 0.09505905]]},
    {'error': 0, 'result': [
        [94054796, 1642813617, 104595.57, 1299074.7, 0.08051544],
        [94054789, 1642813612, 120406.61, 1299074.75, 0.09268644],
        [94054785, 1642788414, 54691.05, 1299074.86, 0.0421],
        [94054793, 1642788417, 635651.6, 1299824.9, 0.48902864],
        [94054612, 1642788336, 6461429.72, 1299824.93, 4.971]]},

    {'error': 0, 'result': [
        [92522256, 1642788418, 203.67, 94034.73, 0.00216591],
        [92522262, 1642788419, 3696.17, 94034.69, 0.0393065],
        [92522235, 1642788410, 564.97, 94034.68, 0.00600815],
        [92522125, 1642788364, 18.79, 93980, 0.0002],
        [92522000, 1642813303, 46939.71, 93950, 0.49962448]]},
    {'error': 0, 'result': [
        [86546274, 1642813603, 31391.56, 94150, 0.33342081],
        [86546272, 1642788419, 8261.11, 94197.46, 0.0877],
        [86546263, 1642788418, 98387.43, 94197.47, 1.04448067],
        [86546257, 1642788415, 14.13, 94197.53, 0.00015004],
        [86546268, 1642788419, 7014907.02, 94317.19, 74.3757]]},

    {'error': 0, 'result': [
        [67300442, 1642813561, 0, 5.1051, 0.00078883],
        [67300100, 1642813405, 0, 5.105, 0.00125533],
        [67300168, 1642788258, 0, 5.105, 0.00080471],
        [67300475, 1642788416, 0.86, 5.1003, 0.168787],
        [67300452, 1642788404, 8.71, 5.1002, 1.70937568]]},
    {'error': 0, 'result': [
        [61056817, 1642813132, 11464.36, 5.11, 2243.51658354],
        [61056849, 1642788420, 19183.15, 5.1179, 3748.2481729],
        [61056831, 1642788407, 5947.62, 5.118, 1162.1],
        [61056843, 1642788417, 113365.58, 5.1195, 22143.87875875],
        [61054058, 1642786636, 638.4, 5.12, 124.6875]]},

    {'error': 0, 'result': [
        [49849577, 1642788420, 7.57, 82.64, 0.091662],
        [49849558, 1642788414, 0.55, 82.6, 0.00669722],
        [49849564, 1642788417, 125.42, 82.59, 1.51868639],
        [49849575, 1642788420, 1.38, 82.49, 0.01684751],
        [49849576, 1642788420, 10.19, 82.49, 0.12362486]]},
    {'error': 0, 'result': [
        [41473295, 1642788420, 102615.69, 82.94, 1237.22801065],
        [41473284, 1642788416, 42926.48, 82.95, 517.49828349],
        [41473290, 1642788418, 7465.5, 82.95, 90],
        [41473291, 1642788419, 6725.6, 82.95, 81.08018023],
        [41468155, 1642786166, 25232.51, 83, 304.00616489]]}]

# print(bitkub_url[0]['result'][0])
# print(bitkub_url[0]['result'][1])
#
# print(bitkub_url[1]['result'][0])
# print(bitkub_url[1]['result'][1])

zonda_url = {'status': 'Ok',
             'sell': [
                 {'ra': '154875.84', 'ca': '0.80122914', 'sa': '0.80122914', 'pa': '0.80122914', 'co': 2},
                 {'ra': '154875.85', 'ca': '0.27010429', 'sa': '0.27010429', 'pa': '0.27010429', 'co': 2},
                 {'ra': '154882.63', 'ca': '0.00006', 'sa': '0.00006', 'pa': '0.00006', 'co': 1},
                 {'ra': '155070.73', 'ca': '0.09199065', 'sa': '0.09199065', 'pa': '0.09199065', 'co': 1},
                 {'ra': '155082.58', 'ca': '0.3', 'sa': '0.3', 'pa': '0.3', 'co': 1},
                 {'ra': '155484.65', 'ca': '1.0227', 'sa': '1.0227', 'pa': '1.0227', 'co': 1},
                 {'ra': '155484.66', 'ca': '7.5134', 'sa': '7.5134', 'pa': '7.5134', 'co': 1},
                 {'ra': '156257.88', 'ca': '0.3000', 'sa': '0.3000', 'pa': '0.3000', 'co': 1},
                 {'ra': '156257.89', 'ca': '3.8156', 'sa': '3.8156', 'pa': '3.8156', 'co': 1},
                 {'ra': '156896.42', 'ca': '0.0063973', 'sa': '0.305511', 'pa': '0.0063973', 'co': 1}],
             'buy': [{'ra': '153200', 'ca': '0.76472748', 'sa': '0.76472748', 'pa': '0.76472748', 'co': 2},
                     {'ra': '153200.11', 'ca': '0.02218398', 'sa': '0.0261097', 'pa': '0.02218398', 'co': 1},
                     {'ra': '153210', 'ca': '0.00231552', 'sa': '0.00231552', 'pa': '0.00231552', 'co': 2},
                     {'ra': '153210.01', 'ca': '0.03544726', 'sa': '0.03544726', 'pa': '0.03544726', 'co': 1},
                     {'ra': '154000', 'ca': '0.00194805', 'sa': '0.00194805', 'pa': '0.00194805', 'co': 1},
                     {'ra': '154000.36', 'ca': '0.03246746', 'sa': '0.03246746', 'pa': '0.03246746', 'co': 1},
                     {'ra': '154005.87', 'ca': '0.00064939', 'sa': '0.00064939', 'pa': '0.00064939', 'co': 1},
                     {'ra': '154005.88', 'ca': '0.01722083', 'sa': '0.01722083', 'pa': '0.01722083', 'co': 1},
                     {'ra': '154005.89', 'ca': '0.2481', 'sa': '0.2481', 'pa': '0.2481', 'co': 1},
                     {'ra': '154200', 'ca': '0.00648508', 'sa': '0.00648508', 'pa': '0.00648508', 'co': 1}],
             'timestamp': '1642790397719', 'seqNo': '91848334'}

zonda_2 = [{'status': 'Ok', 'sell': [{'ra': '154549.99', 'ca': '0.7582', 'sa': '0.7582', 'pa': '0.7582', 'co': 1},
                                     {'ra': '154550', 'ca': '0.00647217', 'sa': '0.0200', 'pa': '0.00647217', 'co': 1},
                                     {'ra': '154692.09', 'ca': '0.01224429', 'sa': '0.01224429', 'pa': '0.01224429',
                                      'co': 1},
                                     {'ra': '154692.10', 'ca': '0.00006000', 'sa': '0.00006000', 'pa': '0.00006000',
                                      'co': 1},
                                     {'ra': '154895', 'ca': '0.00039381', 'sa': '0.00039381', 'pa': '0.00039381',
                                      'co': 1}, {'ra': '154931.78', 'ca': '0.3', 'sa': '0.3', 'pa': '0.3', 'co': 1},
                                     {'ra': '155484.25', 'ca': '1.24063', 'sa': '1.24063', 'pa': '1.24063', 'co': 2},
                                     {'ra': '155484.26', 'ca': '0.04166259', 'sa': '0.04166259', 'pa': '0.04166259',
                                      'co': 1},
                                     {'ra': '155484.43', 'ca': '0.0840385', 'sa': '0.0840385', 'pa': '0.0840385',
                                      'co': 1},
                                     {'ra': '155484.66', 'ca': '7.5134', 'sa': '7.5134', 'pa': '7.5134', 'co': 1}],
            'buy': [{'ra': '153310.01', 'ca': '0.03229755', 'sa': '0.03229755', 'pa': '0.03229755', 'co': 1},
                    {'ra': '153310.07', 'ca': '0.7582', 'sa': '0.7582', 'pa': '0.7582', 'co': 1},
                    {'ra': '153310.08', 'ca': '0.01729899', 'sa': '0.01729899', 'pa': '0.01729899', 'co': 1},
                    {'ra': '154000', 'ca': '0.00629480', 'sa': '0.00629480', 'pa': '0.00629480', 'co': 3},
                    {'ra': '154000.36', 'ca': '0.02041081', 'sa': '0.03246746', 'pa': '0.02041081', 'co': 1},
                    {'ra': '154000.41', 'ca': '0.00308460', 'sa': '0.00308460', 'pa': '0.00308460', 'co': 1},
                    {'ra': '154003', 'ca': '0.00468841', 'sa': '0.00468841', 'pa': '0.00468841', 'co': 2},
                    {'ra': '154050', 'ca': '0.14200376', 'sa': '0.14200376', 'pa': '0.14200376', 'co': 1},
                    {'ra': '154050.07', 'ca': '0.76598928', 'sa': '0.76598928', 'pa': '0.76598928', 'co': 2},
                    {'ra': '154050.08', 'ca': '0.00006', 'sa': '0.00006', 'pa': '0.00006', 'co': 1}],
            'timestamp': '1642792869817', 'seqNo': '91852935'}, {'status': 'Ok', 'sell': [
    {'ra': '11194.89', 'ca': '0.47', 'sa': '0.47', 'pa': '0.47', 'co': 1},
    {'ra': '11195.08', 'ca': '0.21379898', 'sa': '0.21379898', 'pa': '0.21379898', 'co': 1},
    {'ra': '11198.82', 'ca': '0.0008', 'sa': '0.0008', 'pa': '0.0008', 'co': 1},
    {'ra': '11198.88', 'ca': '19.365536', 'sa': '19.365536', 'pa': '19.365536', 'co': 1},
    {'ra': '11198.89', 'ca': '0.26063037', 'sa': '0.3000', 'pa': '0.26063037', 'co': 2},
    {'ra': '11200', 'ca': '1.01651142', 'sa': '1.07200695', 'pa': '1.01651142', 'co': 2},
    {'ra': '11233.45', 'ca': '13.27658', 'sa': '13.27658', 'pa': '13.27658', 'co': 1},
    {'ra': '11233.46', 'ca': '0.52766964', 'sa': '0.52766964', 'pa': '0.52766964', 'co': 2},
    {'ra': '11233.48', 'ca': '8.65684995', 'sa': '8.65684995', 'pa': '8.65684995', 'co': 1},
    {'ra': '11233.52', 'ca': '0.95200004', 'sa': '0.95200004', 'pa': '0.95200004', 'co': 1}], 'buy': [
    {'ra': '11100.1', 'ca': '0.00450446', 'sa': '0.00450446', 'pa': '0.00450446', 'co': 1},
    {'ra': '11110', 'ca': '0.01800180', 'sa': '0.01800180', 'pa': '0.01800180', 'co': 1},
    {'ra': '11111.5', 'ca': '0.06299779', 'sa': '0.06299779', 'pa': '0.06299779', 'co': 1},
    {'ra': '11115', 'ca': '0.00197931', 'sa': '0.00197931', 'pa': '0.00197931', 'co': 1},
    {'ra': '11120', 'ca': '0.08992805', 'sa': '0.08992805', 'pa': '0.08992805', 'co': 1},
    {'ra': '11122.49', 'ca': '0.02000000', 'sa': '0.02000000', 'pa': '0.02000000', 'co': 1},
    {'ra': '11122.5', 'ca': '0.28250000', 'sa': '0.28250000', 'pa': '0.28250000', 'co': 1},
    {'ra': '11122.52', 'ca': '0.46089150', 'sa': '0.46089150', 'pa': '0.46089150', 'co': 1},
    {'ra': '11122.53', 'ca': '1.59033594', 'sa': '1.59033594', 'pa': '1.59033594', 'co': 1},
    {'ra': '11180.00', 'ca': '0.01536315', 'sa': '0.01536315', 'pa': '0.01536315', 'co': 1}],
                                                                 'timestamp': '1642792869447', 'seqNo': '103810273'},
           {'status': 'Ok',
            'sell': [{'ra': '285.84', 'ca': '22.1898381', 'sa': '22.1898381', 'pa': '22.1898381', 'co': 1},
                     {'ra': '285.85', 'ca': '83.2', 'sa': '83.2', 'pa': '83.2', 'co': 1},
                     {'ra': '286.2', 'ca': '98.0', 'sa': '98.0', 'pa': '98.0', 'co': 1},
                     {'ra': '286.92', 'ca': '35.4600', 'sa': '35.4600', 'pa': '35.4600', 'co': 1},
                     {'ra': '286.93', 'ca': '842.6', 'sa': '842.6', 'pa': '842.6', 'co': 1},
                     {'ra': '286.96', 'ca': '165.09893423', 'sa': '165.09893423', 'pa': '165.09893423', 'co': 1},
                     {'ra': '287.34', 'ca': '50.0', 'sa': '50.0', 'pa': '50.0', 'co': 1},
                     {'ra': '287.71', 'ca': '18.47846337', 'sa': '18.47846337', 'pa': '18.47846337', 'co': 1},
                     {'ra': '288.24', 'ca': '160.0000', 'sa': '160.0000', 'pa': '160.0000', 'co': 1},
                     {'ra': '288.25', 'ca': '416.3', 'sa': '416.3', 'pa': '416.3', 'co': 1}],
            'buy': [{'ra': '281', 'ca': '2.39857651', 'sa': '2.39857651', 'pa': '2.39857651', 'co': 1},
                    {'ra': '282', 'ca': '42.57092199', 'sa': '42.57092199', 'pa': '42.57092199', 'co': 2},
                    {'ra': '282.26', 'ca': '834.7', 'sa': '834.7', 'pa': '834.7', 'co': 1},
                    {'ra': '282.52', 'ca': '83.2000000', 'sa': '83.2000000', 'pa': '83.2000000', 'co': 1},
                    {'ra': '282.53', 'ca': '0.39353765', 'sa': '0.39353765', 'pa': '0.39353765', 'co': 1},
                    {'ra': '283', 'ca': '2.00000000', 'sa': '2.00000000', 'pa': '2.00000000', 'co': 1},
                    {'ra': '283.05', 'ca': '50.0', 'sa': '50.0', 'pa': '50.0', 'co': 1},
                    {'ra': '283.06', 'ca': '546.28664401', 'sa': '546.28664401', 'pa': '546.28664401', 'co': 1},
                    {'ra': '283.5', 'ca': '98.0', 'sa': '98.0', 'pa': '98.0', 'co': 1},
                    {'ra': '283.51', 'ca': '527.5448', 'sa': '527.5448', 'pa': '527.5448', 'co': 1}],
            'timestamp': '1642792869956', 'seqNo': '25278473'}, {'status': 'Ok', 'sell': [
        {'ra': '9.99', 'ca': '1982.7944', 'sa': '1982.7944', 'pa': '1982.7944', 'co': 1},
        {'ra': '10.00', 'ca': '659.0', 'sa': '659.0', 'pa': '659.0', 'co': 1},
        {'ra': '10.08', 'ca': '1844.49295276', 'sa': '1844.49295276', 'pa': '1844.49295276', 'co': 1},
        {'ra': '10.09', 'ca': '425.0', 'sa': '425.0', 'pa': '425.0', 'co': 1},
        {'ra': '10.1', 'ca': '6582.71188119', 'sa': '6584.00000000', 'pa': '6582.71188119', 'co': 2},
        {'ra': '10.20', 'ca': '317.60839349', 'sa': '317.60839349', 'pa': '317.60839349', 'co': 2},
        {'ra': '10.54', 'ca': '9.25234605', 'sa': '657.00000000', 'pa': '9.25234605', 'co': 1},
        {'ra': '10.55', 'ca': '940.73377250', 'sa': '940.73377250', 'pa': '940.73377250', 'co': 1},
        {'ra': '10.76', 'ca': '937.82119443', 'sa': '937.82119443', 'pa': '937.82119443', 'co': 1},
        {'ra': '10.77', 'ca': '937.82119443', 'sa': '937.82119443', 'pa': '937.82119443', 'co': 1}], 'buy': [
        {'ra': '9.58', 'ca': '1304.0', 'sa': '1304.0', 'pa': '1304.0', 'co': 1},
        {'ra': '9.6', 'ca': '208.85416667', 'sa': '208.85416667', 'pa': '208.85416667', 'co': 2},
        {'ra': '9.7', 'ca': '133.54432989', 'sa': '133.54432989', 'pa': '133.54432989', 'co': 2},
        {'ra': '9.75', 'ca': '3344.0', 'sa': '3344.0', 'pa': '3344.0', 'co': 1},
        {'ra': '9.80', 'ca': '6795.0', 'sa': '6795.0', 'pa': '6795.0', 'co': 1},
        {'ra': '9.81', 'ca': '659.0', 'sa': '659.0', 'pa': '659.0', 'co': 1},
        {'ra': '9.84', 'ca': '1454.00000000', 'sa': '1454.00000000', 'pa': '1454.00000000', 'co': 2},
        {'ra': '9.88', 'ca': '2008.63377251', 'sa': '2008.63377251', 'pa': '2008.63377251', 'co': 2},
        {'ra': '9.89', 'ca': '24.5799259', 'sa': '24.5799259', 'pa': '24.5799259', 'co': 1},
        {'ra': '9.90', 'ca': '17.50469929', 'sa': '17.50469929', 'pa': '17.50469929', 'co': 1}],
                                                                 'timestamp': '1642792869973', 'seqNo': '8242354'}]
responses = [
    {'status': 'Ok', 'sell': [
        {'ra': '153800', 'ca': '0.39870045', 'sa': '0.4', 'pa': '0.39870045', 'co': 1},
        {'ra': '153898', 'ca': '0.02300634', 'sa': '0.02300634', 'pa': '0.02300634', 'co': 1},
        {'ra': '154036.5', 'ca': '0.00006', 'sa': '0.00006', 'pa': '0.00006', 'co': 1},
        {'ra': '154262.30', 'ca': '0.02448858', 'sa': '0.02448858', 'pa': '0.02448858', 'co': 2},
        {'ra': '154262.31', 'ca': '0.7582', 'sa': '0.7582', 'pa': '0.7582', 'co': 1},
        {'ra': '154769.69', 'ca': '1.0246', 'sa': '1.0246', 'pa': '1.0246', 'co': 1}, {'ra': '154769.71', 'ca': '0.21659', 'sa': '0.21659', 'pa': '0.21659', 'co': 1}, {'ra': '154769.79', 'ca': '0.09370607', 'sa': '0.09370607', 'pa': '0.09370607', 'co': 1}, {'ra': '154769.83', 'ca': '0.03961217', 'sa': '0.03961217', 'pa': '0.03961217', 'co': 1}, {'ra': '154770.00', 'ca': '7.5134', 'sa': '7.5134', 'pa': '7.5134', 'co': 1}], 'buy': [{'ra': '153150', 'ca': '0.00163239', 'sa': '0.00163239', 'pa': '0.00163239', 'co': 1}, {'ra': '153150.01', 'ca': '0.01731707', 'sa': '0.01731707', 'pa': '0.01731707', 'co': 1}, {'ra': '153200', 'ca': '0.00652748', 'sa': '0.00652748', 'pa': '0.00652748', 'co': 1}, {'ra': '153200.11', 'ca': '0.02218398', 'sa': '0.02610970', 'pa': '0.02218398', 'co': 1}, {'ra': '153210', 'ca': '0.00231552', 'sa': '0.00231552', 'pa': '0.00231552', 'co': 2}, {'ra': '153210.02', 'ca': '0.7582', 'sa': '0.7582', 'pa': '0.7582', 'co': 1}, {'ra': '153421.58', 'ca': '0.00006', 'sa': '0.00006', 'pa': '0.00006', 'co': 1}, {'ra': '153486', 'ca': '0.001', 'sa': '0.001', 'pa': '0.001', 'co': 1}, {'ra': '153487.27', 'ca': '0.24700000', 'sa': '0.24700000', 'pa': '0.24700000', 'co': 1}, {'ra': '153487.28', 'ca': '0.04278932', 'sa': '0.04278932', 'pa': '0.04278932', 'co': 1}], 'timestamp': '1642794477572', 'seqNo': '91855942'}, {'status': 'Ok', 'sell': [{'ra': '11186.93', 'ca': '0.94890008', 'sa': '0.94890008', 'pa': '0.94890008', 'co': 1}, {'ra': '11186.94', 'ca': '0.34341782', 'sa': '0.34341782', 'pa': '0.34341782', 'co': 1}, {'ra': '11187.01', 'ca': '0.13000000', 'sa': '0.13000000', 'pa': '0.13000000', 'co': 1}, {'ra': '11187.39', 'ca': '0.47000000', 'sa': '0.47000000', 'pa': '0.47000000', 'co': 1}, {'ra': '11190', 'ca': '0.25671952', 'sa': '0.25671952', 'pa': '0.25671952', 'co': 1}, {'ra': '11195.08', 'ca': '0.19950700', 'sa': '0.21379898', 'pa': '0.19950700', 'co': 1}, {'ra': '11198.89', 'ca': '0.26063037', 'sa': '0.3000', 'pa': '0.26063037', 'co': 2}, {'ra': '11200', 'ca': '1.01651142', 'sa': '1.07200695', 'pa': '1.01651142', 'co': 2}, {'ra': '11216.11', 'ca': '13.23749', 'sa': '13.23749', 'pa': '13.23749', 'co': 2}, {'ra': '11216.12', 'ca': '4.28', 'sa': '4.28', 'pa': '4.28', 'co': 1}], 'buy': [{'ra': '11070.01', 'ca': '6.91938431', 'sa': '6.91938431', 'pa': '6.91938431', 'co': 1}, {'ra': '11080', 'ca': '0.05665415', 'sa': '0.05665415', 'pa': '0.05665415', 'co': 3}, {'ra': '11100', 'ca': '1.10499634', 'sa': '2.24562431', 'pa': '1.10499634', 'co': 6}, {'ra': '11100.1', 'ca': '0.00450446', 'sa': '0.00450446', 'pa': '0.00450446', 'co': 1}, {'ra': '11110', 'ca': '0.01800180', 'sa': '0.01800180', 'pa': '0.01800180', 'co': 1}, {'ra': '11111.5', 'ca': '0.06299779', 'sa': '0.06299779', 'pa': '0.06299779', 'co': 1}, {'ra': '11115', 'ca': '0.00197931', 'sa': '0.00197931', 'pa': '0.00197931', 'co': 1}, {'ra': '11117.50', 'ca': '0.03598021', 'sa': '0.03598021', 'pa': '0.03598021', 'co': 1}, {'ra': '11120.37', 'ca': '0.4567357', 'sa': '0.4567357', 'pa': '0.4567357', 'co': 1}, {'ra': '11120.4', 'ca': '1.55807879', 'sa': '1.55807879', 'pa': '1.55807879', 'co': 1}], 'timestamp': '1642794477631', 'seqNo': '103813188'}, {'status': 'Ok', 'sell': [{'ra': '284.37', 'ca': '21.53968164', 'sa': '21.53968164', 'pa': '21.53968164', 'co': 1}, {'ra': '284.38', 'ca': '83.2', 'sa': '83.2', 'pa': '83.2', 'co': 1}, {'ra': '284.6', 'ca': '98.0', 'sa': '98.0', 'pa': '98.0', 'co': 1}, {'ra': '285.3', 'ca': '227.67557892', 'sa': '227.67557892', 'pa': '227.67557892', 'co': 1}, {'ra': '285.32', 'ca': '35.46000000', 'sa': '35.46000000', 'pa': '35.46000000', 'co': 1}, {'ra': '285.61', 'ca': '50.0', 'sa': '50.0', 'pa': '50.0', 'co': 1}, {'ra': '285.71', 'ca': '18.47846337', 'sa': '18.47846337', 'pa': '18.47846337', 'co': 1}, {'ra': '286.03', 'ca': '842.6', 'sa': '842.6', 'pa': '842.6', 'co': 1}, {'ra': '287.74', 'ca': '160.0000', 'sa': '160.0000', 'pa': '160.0000', 'co': 1}, {'ra': '288.13', 'ca': '416.3', 'sa': '416.3', 'pa': '416.3', 'co': 1}], 'buy': [{'ra': '280.44', 'ca': '1.78291257', 'sa': '1.78291257', 'pa': '1.78291257', 'co': 1}, {'ra': '281', 'ca': '2.39857651', 'sa': '2.39857651', 'pa': '2.39857651', 'co': 1}, {'ra': '281.2', 'ca': '98.00000000', 'sa': '98.00000000', 'pa': '98.00000000', 'co': 1}, {'ra': '281.35', 'ca': '50.0', 'sa': '50.0', 'pa': '50.0', 'co': 1}, {'ra': '281.36', 'ca': '530.55267857', 'sa': '530.55267857', 'pa': '530.55267857', 'co': 2}, {'ra': '282', 'ca': '42.57092199', 'sa': '42.57092199', 'pa': '42.57092199', 'co': 2}, {'ra': '282.55', 'ca': '10.01312646', 'sa': '10.5', 'pa': '10.01312646', 'co': 1}, {'ra': '282.6', 'ca': '3.06698514', 'sa': '3.06698514', 'pa': '3.06698514', 'co': 1}, {'ra': '283', 'ca': '45.67632509', 'sa': '45.67632509', 'pa': '45.67632509', 'co': 1}, {'ra': '283.01', 'ca': '472.76059', 'sa': '472.76059', 'pa': '472.76059', 'co': 1}], 'timestamp': '1642794477633', 'seqNo': '25280825'}, {'status': 'Ok', 'sell': [{'ra': '9.86', 'ca': '2.92238010', 'sa': '2.92238010', 'pa': '2.92238010', 'co': 1}, {'ra': '9.87', 'ca': '670.0', 'sa': '670.0', 'pa': '670.0', 'co': 1}, {'ra': '9.9', 'ca': '2024.6525', 'sa': '2024.6525', 'pa': '2024.6525', 'co': 1}, {'ra': '9.93', 'ca': '145.00260417', 'sa': '145.00260417', 'pa': '145.00260417', 'co': 1}, {'ra': '9.95', 'ca': '415.00000000', 'sa': '415.00000000', 'pa': '415.00000000', 'co': 1}, {'ra': '9.96', 'ca': '8422.49295276', 'sa': '8422.49295276', 'pa': '8422.49295276', 'co': 2}, {'ra': '10.1', 'ca': '3.71188119', 'sa': '5.00000000', 'pa': '3.71188119', 'co': 1}, {'ra': '10.20', 'ca': '317.60839349', 'sa': '317.60839349', 'pa': '317.60839349', 'co': 2}, {'ra': '10.54', 'ca': '9.25234605', 'sa': '657.00000000', 'pa': '9.25234605', 'co': 1}, {'ra': '10.55', 'ca': '940.73377250', 'sa': '940.73377250', 'pa': '940.73377250', 'co': 1}], 'buy': [{'ra': '9.6', 'ca': '208.85416667', 'sa': '208.85416667', 'pa': '208.85416667', 'co': 2}, {'ra': '9.65', 'ca': '200.0', 'sa': '200.0', 'pa': '200.0', 'co': 1}, {'ra': '9.67', 'ca': '3344.0', 'sa': '3344.0', 'pa': '3344.0', 'co': 1}, {'ra': '9.68', 'ca': '6585.0', 'sa': '6585.0', 'pa': '6585.0', 'co': 1}, {'ra': '9.7', 'ca': '93.78041237', 'sa': '93.78041237', 'pa': '93.78041237', 'co': 2}, {'ra': '9.71', 'ca': '670.0', 'sa': '670.0', 'pa': '670.0', 'co': 1}, {'ra': '9.72', 'ca': '845.00000000', 'sa': '845.00000000', 'pa': '845.00000000', 'co': 1}, {'ra': '9.76', 'ca': '612.0', 'sa': '612.0', 'pa': '612.0', 'co': 1}, {'ra': '9.77', 'ca': '554.36829804', 'sa': '554.36829804', 'pa': '554.36829804', 'co': 2}, {'ra': '9.79', 'ca': '1500.0', 'sa': '1500.0', 'pa': '1500.0', 'co': 1}], 'timestamp': '1642794477670', 'seqNo': '8244212'}]



# print(f"{str(responses[0]['sell'][0]['ra'])}")
#
#
#
# a = {'one': "sth",
#      "two": "more",
#      "three": "data"}
#
# print(len(responses))
#
# print(list(a.keys()).index("two"))
#
# print(list(range(0,4)))
#
#
# d = {'btcpln': "rading/orderbook-limited/['btcpln']}/10",
#      'ethpln': "'ethpln']}/10",
#      'lunapln': "unapln']}/10",
#      'ftmpln': "ftmpln']}/10"}
#
# print(list(d.keys())[0])

tr = {"action":"push",
      "topic":"trading/transactions/eth-pln",
      "message":{
          "transactions":[
              {"id":"be329f75-7b63-11ec-9be8-0242ac110009","t":"1642842886461","a":"1.12074687","r":"9800.15","ty":"Buy"}]},
      "timestamp":"1642842886461","seqNo":2109232}

# print(tr['topic'].split('/')[2].replace("-", ""))
# print(tr['message']['transactions'][0]['id'])
# print(tr['message']['transactions'][0]['r'])
# print(tr['message']['transactions'][0]['a'])
# print(tr['timestamp'])

k = {'amt': 16.99318568,
     'bid': 2852532,
     'rat': 6.27,
     'sid': 2665037,
     'stream': 'market.trade.thb_gala',
     'sym': 'THB_GALA',
     'ts': 1642860084,
     'txn': 'GALASELL0000876211'}

print(k['txn'])
print(k['rat'])
print(k['amt'])
print(k['ts']*1000)

print(f"{k['stream'].split('_')[1]}thb_trades")
