# coding: utf-8

import os
import sys
import time


# base_dir = os.path.dirname(__file__)
# sys.path.insert(0, base_dir)
# sys.path.append(os.path.dirname(base_dir))


from . import GL, __version__
from .low import *
from .args import parse_args
from . import __version__
from .logic import read_sectors, write_sectors, verify_sectors, danger_verify_sectors
from .error_handler import process_errors


def entry_point():

    args = parse_args(sys.argv[1:])
    GL.block_device_path = args.device_path
    GL.args = args
    GL.version = __version__

    if os.geteuid() != 0:
        print("\n\tRun it as root. \n")
        exit()
    elif args.action == "read":
        errors = read_sectors()
        process_errors(errors)
    elif args.action == "write":
        errors = write_sectors()
        process_errors(errors)
    elif args.action == "verify":
        errors = verify_sectors()
        process_errors(errors)
    elif args.action == "danger_verify":
        errors = danger_verify_sectors()
        process_errors(errors)
    else:
        print("Failed successfully: entry_point. Exiting...")
        exit(-1)


    # with open(block_device_path, "rb+") as block_device:
    #     GL.bd = block_device
    #     sectors_num = get_sectors_num(block_device)
    #     pbar = tqdm(range(sectors_num))
    #     for i in pbar:
    #         try:
    #             bs = read_sector(block_device, i)
    #         except OSError as e:
    #             if e.errno == 5:
    #                 print(f"Input/output error: {i}")
    #
    #         if not i % 1024:
    #             pbar.set_postfix({"MB": f'{(i*512)/(1024*1024):.2f}'}) # 21035336 # 21035336
"""
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/run/media/the220th/archBTW/home/the220th/git/disk_block_check/disk_block_check/__main__.py", line 16, in <module>
    sys.exit(main())
             ^^^^^^
  File "/run/media/the220th/archBTW/home/the220th/git/disk_block_check/disk_block_check/main.py", line 27, in main
    bs = read_sector(block_device, i)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/run/media/the220th/archBTW/home/the220th/git/disk_block_check/disk_block_check/low.py", line 71, in read_sector
    res = block_device.read(SECTOR_SIZE)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 5] Input/output error
"""

"""
> sudo python -m disk_block_check

        Run it as root.

  1%|█▌                                                                                                                                                | 21032893/1953525168 [01:11<1:50:47, 290687.89it/s, MB=1283.87]Input/output error: 21035336
Input/output error: 21035337
Input/output error: 21035338
Input/output error: 21035339
Input/output error: 21035340
  1%|█▌                                                                                                                                                | 21032893/1953525168 [01:30<1:50:47, 290687.89it/s, MB=1283.87]Input/output error: 21035341
  1%|█▌                                                                                                                                                | 21035342/1953525168 [01:30<144:42:25, 3709.58it/s, MB=1283.87]Input/output error: 21035342
Input/output error: 21035343
 11%|████████████████▎                                                                                                                                | 218981314/1953525168 [58:07<8:15:03, 58395.81it/s, MB=13365.66]Input/output error: 218983912
Input/output error: 218983913
Input/output error: 218983914
 11%|████████████████▎                                                                                                                                | 218981314/1953525168 [58:20<8:15:03, 58395.81it/s, MB=13365.66]Input/output error: 218983915
 11%|████████████████▏                                                                                                                               | 218983916/1953525168 [58:21<386:30:57, 1246.56it/s, MB=13365.66]Input/output error: 218983916
Input/output error: 218983917
Input/output error: 218983918
Input/output error: 218983919
 11%|████████████████▌                                                                                                                                | 222838089/1953525168 [59:42<9:15:41, 51908.32it/s, MB=13601.20]Input/output error: 222842648
Input/output error: 222842649
Input/output error: 222842650
Input/output error: 222842651
Input/output error: 222842652
 11%|████████████████▎                                                                                                                              | 222838089/1953525168 [1:00:00<9:15:41, 51908.32it/s, MB=13601.20]Input/output error: 222842653
 11%|████████████████▎                                                                                                                              | 222842654/1953525168 [1:00:01<503:43:16, 954.39it/s, MB=13601.20]Input/output error: 222842654
Input/output error: 222842655
 12%|████████████████▌                                                                                                                              | 226369169/1953525168 [1:01:09<9:18:11, 51569.22it/s, MB=13816.65]Input/output error: 226372032
Input/output error: 226372033
 12%|████████████████▌                                                                                                                              | 226369169/1953525168 [1:01:20<9:18:11, 51569.22it/s, MB=13816.65]Input/output error: 226372034
 12%|████████████████▍                                                                                                                             | 226372035/1953525168 [1:01:20<336:02:07, 1427.72it/s, MB=13816.65]Input/output error: 226372035
Input/output error: 226372036
Input/output error: 226372037
Input/output error: 226372038
Input/output error: 226372039
 24%|██████████████████████████████████▌                                                                                                            | 471815423/1953525168 [2:12:03<8:19:37, 49427.55it/s, MB=28797.36]Input/output error: 471816256
Input/output error: 471816257
Input/output error: 471816258
Input/output error: 471816259
Input/output error: 471816260
 24%|██████████████████████████████████▌                                                                                                            | 471815423/1953525168 [2:12:20<8:19:37, 49427.55it/s, MB=28797.36]Input/output error: 471816261
 24%|██████████████████████████████████▌                                                                                                            | 471816262/1953525168 [2:12:21<602:43:17, 682.88it/s, MB=28797.36]Input/output error: 471816262
Input/output error: 471816263
 24%|██████████████████████████████████▌                                                                                                            | 471914859/1953525168 [2:12:29<8:32:03, 48224.38it/s, MB=28803.59]Input/output error: 471918408
Input/output error: 471918409
 24%|██████████████████████████████████▌                                                                                                            | 471914859/1953525168 [2:12:40<8:32:03, 48224.38it/s, MB=28803.59]Input/output error: 471918410
 24%|██████████████████████████████████▎                                                                                                           | 471918411/1953525168 [2:12:40<296:28:40, 1388.16it/s, MB=28803.59]Input/output error: 471918411
Input/output error: 471918412
Input/output error: 471918413
Input/output error: 471918414
Input/output error: 471918415
 24%|██████████████████████████████████▋                                                                                                            | 473309317/1953525168 [2:13:21<8:55:42, 46051.77it/s, MB=28888.55]Input/output error: 473310216
Input/output error: 473310217
Input/output error: 473310218
Input/output error: 473310219
Input/output error: 473310220
 24%|██████████████████████████████████▋                                                                                                            | 473309317/1953525168 [2:13:40<8:55:42, 46051.77it/s, MB=28888.55]Input/output error: 473310221
 24%|██████████████████████████████████▋                                                                                                            | 473310222/1953525168 [2:13:40<619:17:10, 663.94it/s, MB=28888.55]Input/output error: 473310222
Input/output error: 473310223
 24%|██████████████████████████████████▊                                                                                                            | 475612233/1953525168 [2:14:29<7:58:38, 51461.39it/s, MB=29029.30]Input/output error: 475616296
Input/output error: 475616297
Input/output error: 475616298
 24%|██████████████████████████████████▊                                                                                                            | 475612233/1953525168 [2:14:40<7:58:38, 51461.39it/s, MB=29029.30]Input/output error: 475616299
 24%|██████████████████████████████████▌                                                                                                           | 475616300/1953525168 [2:14:42<347:08:48, 1182.58it/s, MB=29029.30]Input/output error: 475616300
Input/output error: 475616301
Input/output error: 475616302
Input/output error: 475616303
 24%|██████████████████████████████████▊                                                                                                            | 475649153/1953525168 [2:14:54<64:21:20, 6378.95it/s, MB=29031.49]Input/output error: 475652152
Input/output error: 475652153
Input/output error: 475652154
Input/output error: 475652155
 24%|██████████████████████████████████▊                                                                                                            | 475649153/1953525168 [2:15:10<64:21:20, 6378.95it/s, MB=29031.49]Input/output error: 475652156
 24%|██████████████████████████████████▊                                                                                                            | 475652157/1953525168 [2:15:10<491:46:24, 834.78it/s, MB=29031.49]Input/output error: 475652157
Input/output error: 475652158
Input/output error: 475652159
 24%|██████████████████████████████████▌                                                                                                           | 475720937/1953525168 [2:15:20<12:18:51, 33335.68it/s, MB=29035.89]Input/output error: 475724960
Input/output error: 475724961
Input/output error: 475724962
Input/output error: 475724963
Input/output error: 475724964
Input/output error: 475724965
 24%|██████████████████████████████████▌                                                                                                           | 475720937/1953525168 [2:15:40<12:18:51, 33335.68it/s, MB=29035.89]Input/output error: 475724966
 24%|██████████████████████████████████▊                                                                                                            | 475724967/1953525168 [2:15:42<550:04:04, 746.27it/s, MB=29035.89]Input/output error: 475724967
 24%|██████████████████████████████████▊                                                                                                            | 475815631/1953525168 [2:15:47<9:15:24, 44343.27it/s, MB=29041.44]Input/output error: 475815992
Input/output error: 475815993
Input/output error: 475815994
 24%|██████████████████████████████████▊                                                                                                            | 475815631/1953525168 [2:16:00<9:15:24, 44343.27it/s, MB=29041.44]Input/output error: 475815995
 24%|██████████████████████████████████▊                                                                                                            | 475815996/1953525168 [2:16:00<458:24:55, 895.42it/s, MB=29041.44]Input/output error: 475815996
Input/output error: 475815997
Input/output error: 475815998
 24%|██████████████████████████████████▊                                                                                                            | 475815999/1953525168 [2:16:09<858:30:23, 478.13it/s, MB=29041.44]Input/output error: 475815999
 24%|██████████████████████████████████▊                                                                                                            | 475906347/1953525168 [2:16:13<9:51:41, 41621.02it/s, MB=29047.00]Input/output error: 475906368
Input/output error: 475906369
Input/output error: 475906370
Input/output error: 475906371
 24%|██████████████████████████████████▊                                                                                                            | 475906347/1953525168 [2:16:30<9:51:41, 41621.02it/s, MB=29047.00]Input/output error: 475906372
 24%|██████████████████████████████████▊                                                                                                            | 475906373/1953525168 [2:16:30<517:28:48, 793.17it/s, MB=29047.00]Input/output error: 475906373
 24%|██████████████████████████████████▊                                                                                                            | 475906374/1953525168 [2:16:32<626:52:30, 654.76it/s, MB=29047.00]Input/output error: 475906374
Input/output error: 475906375
 24%|██████████████████████████████████▌                                                                                                           | 475988311/1953525168 [2:16:40<10:28:16, 39195.26it/s, MB=29052.00]Input/output error: 475988672
Input/output error: 475988673
Input/output error: 475988674
Input/output error: 475988675
Input/output error: 475988676
Input/output error: 475988677
 24%|██████████████████████████████████▌                                                                                                           | 475988311/1953525168 [2:17:00<10:28:16, 39195.26it/s, MB=29052.00]Input/output error: 475988678
 24%|██████████████████████████████████▊                                                                                                            | 475988679/1953525168 [2:17:01<732:25:27, 560.37it/s, MB=29052.00]Input/output error: 475988679
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1953525168/1953525168 [9:36:59<00:00, 56427.90it/s, MB=119233.70]
"""



"""
12:52:49 : Starting Victoria 5.28 HDD/SSD. 2xCPU, 1338.00 MHz, Windows 10 x64 found.
12:52:49 : [Hint] Recommend 32-bit Windows XP for a best work!
12:52:49 : Warning! Windows x64 detected! PIO mode supported on Windows x86 only.
12:52:49 : API access enabled, device #0
12:52:49 : Get drive passport... OK
12:52:50 : Model: ST1000NM0011; Capacity: 1953525168 LBAs; SN: Z1N45XZG; FW: SN03
12:52:50 : Press F1 to About/HELP
12:53:01 : Get drive passport... OK
12:53:01 : Model: ST1000NM0011; Capacity 1953525168 LBAs; SN: Z1N45XZG; FW: SN03
12:53:02 : Get S.M.A.R.T. command... OK
12:53:02 : SMART base updated.
12:53:03 : SMART status = GOOD
12:53:09 : Get drive passport... OK
12:53:10 : Recallibration... OK
12:53:10 : Starting Reading, LBA=0..1953525167, FULL, sequential access, timeout 10000ms
1:00:25  : Block start at 21035008 (11 GB) Read error: UNCR "Data error (cyclic redundancy check)"
2:08:45  : Block start at 218982400 (112 GB) Read error: UNCR "Data error (cyclic redundancy check)"
2:10:08  : Block start at 222840832 (114 GB) Read error: UNCR "Data error (cyclic redundancy check)"
2:11:26  : Block start at 226371584 (116 GB) Read error: UNCR "Data error (cyclic redundancy check)"
3:36:15  : Block start at 471816192 (242 GB) Read error: UNCR "Data error (cyclic redundancy check)"
3:36:22  : Block start at 471916544 (242 GB) Read error: UNCR "Data error (cyclic redundancy check)"
3:36:56  : Block start at 473309184 (242 GB) Read error: UNCR "Data error (cyclic redundancy check)"
3:37:47  : Block start at 475615232 (244 GB) Read error: UNCR "Data error (cyclic redundancy check)"
3:37:53  : Block start at 475652096 (244 GB) Read error: UNCR "Data error (cyclic redundancy check)"
3:37:57  : Block start at 475723776 (244 GB) Read error: UNCR "Data error (cyclic redundancy check)"
3:38:01  : Block start at 475815936 (244 GB) Read error: UNCR "Data error (cyclic redundancy check)"
3:38:08  : Block start at 475906048 (244 GB) Read error: UNCR "Data error (cyclic redundancy check)"
3:38:14  : Block start at 475987968 (244 GB) Read error: UNCR "Data error (cyclic redundancy check)"
12:10:18 : *** Scan results: Warnings - 0, errors - 13. Last block at 1953525167 (1.0 TB), time 11 hours 17 minutes 9 seconds.
12:10:18 : Speed: Maximum 27 MB/s. Average 13 MB/s. Minimum 0 MB/s. 405 points.
"""
