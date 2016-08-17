# coding: utf-8

from __future__ import print_function
import requests

API_URL = 'http://{hostname}/cgi-bin/{method}'
API_URL_SET = 'http://{hostname}/cgi-bin/dset.cgi'
API_URL_GET = 'http://{hostname}/cgi-bin/dget.cgi'
API_URL_AJAX_GET = 'http://{hostname}/cgi-bin/ajax_get.cgi'


class Dwr932(object):
    def __init__(self, hostname='192.168.0.1'):
        self.hostname = hostname

    def __api_req(self, method, url , data):
        # print(method, url, data)
        if method.lower() == 'post':
            r = requests.request(method=method, url=url, data=data)
        elif method.lower() == 'get':
            r = requests.request(method=method, url=url, params=data)
        if r.ok:
            return r.json()

    def __api_req_set(self, data):
        return self.__api_req(
            'post', url=API_URL_SET.format(hostname=self.hostname), data=data
        )

    def __api_req_get(self, data):
        return self.__api_req(
            'get', url=API_URL_GET.format(hostname=self.hostname), data=data
        )

    def shutdown(self):
        return self.__api_req(
            'get', url=API_URL_AJAX_GET.format(hostname=self.hostname),
            data='which_ajax=ajax_shutdown_system&pram=shutdown'
        )

    def reboot(self):
        return self.__api_req(
            'get', url=API_URL_AJAX_GET.format(hostname=self.hostname),
            data='which_ajax=ajax_reboot_system&pram=reboot'
        )

    def connect(self):
        return self.__api_req_set(data={'goformId': 'CONNECT_NETWORK'})

    def disconnect(self):
        return self.__api_req_set(data={'goformId': 'DISCONNECT_NETWORK'})

    def get_data_usage(self):
        cmd = 'nw_usage_start,nw_usage_end,DEVICE_sent_bytes,DEVICE_recv_bytes,'
        'DEVICE_live_time,nw_usage_reach'
        return self.__api_req_get(data={'cmd': cmd})

    def get_wifi_info(self):
        cmd = 'wifi_AP1_ssid,wifi_AP1_hidden,wifi_AP1_passphrase,'
        'wifi_AP1_passphrase_wep,wifi_AP1_security_mode,wifi_AP1_enable,'
        'get_mac_filter_list,get_mac_filter_switch,get_client_list,'
        'get_mac_address,get_wps_dev_pin,get_wps_mode,get_wps_enable,'
        'get_wps_current_time'
        return self.__api_req_get(data={'cmd': cmd})

    def get_network_info(self):
        cmd ='ipv4_status,wan_ipaddr,wan_ipaddripv6,roaming_state,'
        'signal_wifi_level,signal_modem_strength,signal_modem_level,'
        'signal_modem_service,signal_modem_op_name,battery_capacity,pin_status,'
        'clientNum_ssid1,DEVICE_currenttime'
        return self.__api_req_get(data={'cmd': cmd})

    def get_sms(self):
        cmd = 'sms_dev_cur_draft_item,sms_dev_cur_item,sms_sim_cur_item'
        return self.__api_req_get(data={'cmd': cmd})

    def get_admin_account(self):
        cmd = 'DEVICE_web_usrname,DEVICE_web_passwd,DEVICE_login_timeout'
        return self.__api_req_get(data={'cmd': cmd})

    def get_device_info(self):
        cmd = 'sw_version,modem_version,hw_version,imei_number,imsi_number,'
        'model_name,system_uptime'
        return self.__api_req_get(data={'cmd': cmd})

    def get_battery_info(self):
        '''
        Get the current battery capacity (in percent)
        NOTE: The battery_status field probably holds the number of "bars" left
        '''
        cmd = 'capacity,battery_status'
        return self.__api_req_get(data={'cmd': cmd})

    def get_power_management(self):
        cmd = 'device_power_suspend,device_power_deepsleep'
        return self.__api_req_get(data={'cmd': cmd})

    def get_upnp_setting(self):
        cmd = 'upnpEnabled'
        return self.__api_req_get(data={'cmd': cmd})
