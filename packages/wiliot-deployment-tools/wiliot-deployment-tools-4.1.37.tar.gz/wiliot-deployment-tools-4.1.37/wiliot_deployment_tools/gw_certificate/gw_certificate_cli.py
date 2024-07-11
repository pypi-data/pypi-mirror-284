from argparse import ArgumentParser
from wiliot_deployment_tools.gw_certificate.gw_certificate import GWCertificate
from wiliot_deployment_tools.gw_certificate.tests import TESTS
import sys
from wiliot_deployment_tools.interface.if_defines import MOVE_TO_BL
from wiliot_deployment_tools.common.debug import debug_print

def filter_tests(tests_names):
    chosen_tests = []
    if tests_names == []:
        return TESTS
    for test_class in TESTS:
        for test_name in tests_names:
            if test_name in test_class.__name__.lower() and test_class not in chosen_tests:
                chosen_tests.append(test_class)
    return chosen_tests

def main():
    parser = ArgumentParser(prog='wlt-gw-certificate',
                            description='Gateway Certificate - CLI Tool to test Wiliot GWs')
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    optional.add_argument('-move_to_bootloader', action='store_true', help="Move the GW to bootloader to enable nordic DFU", default=False, required=False)
    required.add_argument('-owner', type=str, help="Owner ID", required='-move_to_bootloader' not in sys.argv)
    required.add_argument('-gw', type=str, help="Gateway ID", required='-move_to_bootloader' not in sys.argv)
    
    optional.add_argument('-suffix', type=str, help="Topic suffix", default='', required=False)
    optional.add_argument('-coupled', action='store_true', help="GW Metadata Coupling Enabled", default=False, required=False)
    optional.add_argument('-tests', type=str, choices=['connection', 'uplink', 'downlink'], help="Tests to run", required=False, nargs='+', default=[])
    args = parser.parse_args()
    tests = filter_tests(args.tests)
    topic_suffix = '' if args.suffix == '' else '-'+args.suffix

    gwc = GWCertificate(gw_id=args.gw, owner_id=args.owner, coupled=args.coupled, topic_suffix=topic_suffix, tests=tests)

    if args.move_to_bootloader is True:
        gwc.uart.write_ble_command(MOVE_TO_BL)
        debug_print("Arg move_to_bootloader detected - moving the board to bootloader and exiting..")
        return

    gwc.run_tests()
    gwc.create_results_html()

def main_cli():
    main()

if __name__ == '__main__':
    main()
    