myPropertyFile = "conf.properties"

print '======= Reading Property File and Connecting to Server ========'
loadProperties(myPropertyFile)

print '======= Connecting to Server ========'
connect(userConfigFile=userCF, userKeyFile=userKF, url=host)

edit()
startEdit()

#Config XML backuping
cd('/')
cmo.setArchiveConfigurationCount(10)
cmo.setConfigBackupEnabled(true)

#Admin Server
#cd('/Servers/adm_wl11_by_' + ENV + '/ServerStart/adm_wl11_by_' + ENV + '')
#cmo.setArguments('-Xms768m -Xmx768m -Xmanagement:port=15901 -Dweblogic.management.disableManagedServerNotifications=true -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Dweblogic.Stdout=/log/fmw/adminserver/adm_wl11_by_' + ENV + '/stdout.log -Dweblogic.Stderr=/log/fmw/adminserver/adm_wl11_by_' + ENV + '/stderr.log -Xverbose:gc=info,memory=info -XverboseLog:/log/fmw/adminserver/adm_wl11_by_' + ENV + '/jrockit.log -XX:+HeapDiagnosticsOnOutOfMemoryError -XX:HeapDumpPath=/dumps -XX:+HeapDumpOnCtrlBreak -XX:+HeapDumpOnOutOfMemoryError -Dweblogic.webservice.i18n.charset=utf-8 -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -Djava.awt.headless=true')


#Cif Cluster
cd('/Servers/wl_by_' + ENV + '_01_cif/ServerStart/wl_by_' + ENV + '_01_cif')
cmo.setArguments('-Xms512m -Xmx512m -Xmanagement:port=5901 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Dweblogic.Stdout=/log/fmw/managedservers/wl_by_' + ENV + '_01_cif/stdout.log -Dweblogic.Stderr=/log/fmw/managedservers/wl_by_' + ENV + '_01_cif/stderr.log -Xverbose:gc=info,memory=info -XverboseLog:/log/fmw/managedservers/wl_by_' + ENV + '_01_cif/jrockit.log -XX:+HeapDiagnosticsOnOutOfMemoryError -XX:HeapDumpPath=/dumps -XX:+HeapDumpOnCtrlBreak -XX:+HeapDumpOnOutOfMemoryError -Dweblogic.webservice.i18n.charset=utf-8 -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -Djava.awt.headless=true -Duser.language=ru -Duser.country=RU')

cd('/Servers/wl_by_' + ENV + '_02_cif/ServerStart/wl_by_' + ENV + '_02_cif')
cmo.setArguments('-Xms512m -Xmx512m -Xmanagement:port=5901 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Dweblogic.Stdout=/log/fmw/managedservers/wl_by_' + ENV + '_02_cif/stdout.log -Dweblogic.Stderr=/log/fmw/managedservers/wl_by_' + ENV + '_02_cif/stderr.log -Xverbose:gc=info,memory=info -XverboseLog:/log/fmw/managedservers/wl_by_' + ENV + '_02_cif/jrockit.log -XX:+HeapDiagnosticsOnOutOfMemoryError -XX:HeapDumpPath=/dumps -XX:+HeapDumpOnCtrlBreak -XX:+HeapDumpOnOutOfMemoryError -Dweblogic.webservice.i18n.charset=utf-8 -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -Djava.awt.headless=true -Duser.language=ru -Duser.country=RU')

#HOMEB Cluster
cd('/Servers/wl_by_' + ENV + '_01_homeb/ServerStart/wl_by_' + ENV + '_01_homeb')
cmo.setArguments('-Xms512m -Xmx512m -Xmanagement:port=5902 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Dweblogic.Stdout=/log/fmw/managedservers/wl_by_' + ENV + '_01_homeb/stdout.log -Dweblogic.Stderr=/log/fmw/managedservers/wl_by_' + ENV + '_01_homeb/stderr.log -Xverbose:gc=info,memory=info -XverboseLog:/log/fmw/managedservers/wl_by_' + ENV + '_01_homeb/jrockit.log -XX:+HeapDiagnosticsOnOutOfMemoryError -XX:HeapDumpPath=/dumps -XX:+HeapDumpOnCtrlBreak -XX:+HeapDumpOnOutOfMemoryError -Dweblogic.webservice.i18n.charset=utf-8 -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -Djava.awt.headless=true -Duser.language=ru -Duser.country=RU')

cd('/Servers/wl_by_' + ENV + '_02_homeb/ServerStart/wl_by_' + ENV + '_02_homeb')
cmo.setArguments('-Xms512m -Xmx512m -Xmanagement:port=5902 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Dweblogic.Stdout=/log/fmw/managedservers/wl_by_' + ENV + '_02_homeb/stdout.log -Dweblogic.Stderr=/log/fmw/managedservers/wl_by_' + ENV + '_02_homeb/stderr.log -Xverbose:gc=info,memory=info -XverboseLog:/log/fmw/managedservers/wl_by_' + ENV + '_02_homeb/jrockit.log -XX:+HeapDiagnosticsOnOutOfMemoryError -XX:HeapDumpPath=/dumps -XX:+HeapDumpOnCtrlBreak -XX:+HeapDumpOnOutOfMemoryError -Dweblogic.webservice.i18n.charset=utf-8 -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -Djava.awt.headless=true -Duser.language=ru -Duser.country=RU')

#HOMEB_WS Cluster
cd('/Servers/wl_by_' + ENV + '_01_homeb_ws/ServerStart/wl_by_' + ENV + '_01_homeb_ws')
cmo.setArguments('-Xms512m -Xmx512m -Xmanagement:port=5903 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Dweblogic.Stdout=/log/fmw/managedservers/wl_by_' + ENV + '_01_homeb_ws/stdout.log -Dweblogic.Stderr=/log/fmw/managedservers/wl_by_' + ENV + '_01_homeb_ws/stderr.log -Xverbose:gc=info,memory=info -XverboseLog:/log/fmw/managedservers/wl_by_' + ENV + '_01_homeb_ws/jrockit.log -XX:+HeapDiagnosticsOnOutOfMemoryError -XX:HeapDumpPath=/dumps -XX:+HeapDumpOnCtrlBreak -XX:+HeapDumpOnOutOfMemoryError -Dweblogic.webservice.i18n.charset=utf-8 -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -Djava.awt.headless=true -Duser.language=ru -Duser.country=RU')

cd('/Servers/wl_by_' + ENV + '_02_homeb_ws/ServerStart/wl_by_' + ENV + '_02_homeb_ws')
cmo.setArguments('-Xms512m -Xmx512m -Xmanagement:port=5903 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Dweblogic.Stdout=/log/fmw/managedservers/wl_by_' + ENV + '_02_homeb_ws/stdout.log -Dweblogic.Stderr=/log/fmw/managedservers/wl_by_' + ENV + '_02_homeb_ws/stderr.log -Xverbose:gc=info,memory=info -XverboseLog:/log/fmw/managedservers/wl_by_' + ENV + '_02_homeb_ws/jrockit.log -XX:+HeapDiagnosticsOnOutOfMemoryError -XX:HeapDumpPath=/dumps -XX:+HeapDumpOnCtrlBreak -XX:+HeapDumpOnOutOfMemoryError -Dweblogic.webservice.i18n.charset=utf-8 -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -Djava.awt.headless=true -Duser.language=ru -Duser.country=RU')

#JMS Cluster
cd('/Servers/wl_by_' + ENV + '_01_jms/ServerStart/wl_by_' + ENV + '_01_jms')
cmo.setArguments('-Xms512m -Xmx512m -Xmanagement:port=5904 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Dweblogic.Stdout=/log/fmw/managedservers/wl_by_' + ENV + '_01_jms/stdout.log -Dweblogic.Stderr=/log/fmw/managedservers/wl_by_' + ENV + '_01_jms/stderr.log -Xverbose:gc=info,memory=info -XverboseLog:/log/fmw/managedservers/wl_by_' + ENV + '_01_jms/jrockit.log -XX:+HeapDiagnosticsOnOutOfMemoryError -XX:HeapDumpPath=/dumps -XX:+HeapDumpOnCtrlBreak -XX:+HeapDumpOnOutOfMemoryError -Dweblogic.webservice.i18n.charset=utf-8 -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -Djava.awt.headless=true -Duser.language=ru -Duser.country=RU')

cd('/Servers/wl_by_' + ENV + '_02_jms/ServerStart/wl_by_' + ENV + '_02_jms')
cmo.setArguments('-Xms512m -Xmx512m -Xmanagement:port=5904 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Dweblogic.Stdout=/log/fmw/managedservers/wl_by_' + ENV + '_02_jms/stdout.log -Dweblogic.Stderr=/log/fmw/managedservers/wl_by_' + ENV + '_02_jms/stderr.log -Xverbose:gc=info,memory=info -XverboseLog:/log/fmw/managedservers/wl_by_' + ENV + '_02_jms/jrockit.log -XX:+HeapDiagnosticsOnOutOfMemoryError -XX:HeapDumpPath=/dumps -XX:+HeapDumpOnCtrlBreak -XX:+HeapDumpOnOutOfMemoryError -Dweblogic.webservice.i18n.charset=utf-8 -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -Djava.awt.headless=true -Duser.language=ru -Duser.country=RU')

#MSG Cluster
cd('/Servers/wl_by_' + ENV + '_01_msg/ServerStart/wl_by_' + ENV + '_01_msg')
cmo.setArguments('-Xms256m -Xmx256m -Xmanagement:port=5905 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Dweblogic.Stdout=/log/fmw/managedservers/wl_by_' + ENV + '_01_msg/stdout.log -Dweblogic.Stderr=/log/fmw/managedservers/wl_by_' + ENV + '_01_msg/stderr.log -Xverbose:gc=info,memory=info -XverboseLog:/log/fmw/managedservers/wl_by_' + ENV + '_01_msg/jrockit.log -XX:+HeapDiagnosticsOnOutOfMemoryError -XX:HeapDumpPath=/dumps -XX:+HeapDumpOnCtrlBreak -XX:+HeapDumpOnOutOfMemoryError -Dweblogic.webservice.i18n.charset=utf-8 -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -Djava.awt.headless=true -Duser.language=ru -Duser.country=RU')

cd('/Servers/wl_by_' + ENV + '_02_msg/ServerStart/wl_by_' + ENV + '_02_msg')
cmo.setArguments('-Xms256m -Xmx256m -Xmanagement:port=5905 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Dweblogic.Stdout=/log/fmw/managedservers/wl_by_' + ENV + '_02_msg/stdout.log -Dweblogic.Stderr=/log/fmw/managedservers/wl_by_' + ENV + '_02_msg/stderr.log -Xverbose:gc=info,memory=info -XverboseLog:/log/fmw/managedservers/wl_by_' + ENV + '_02_msg/jrockit.log -XX:+HeapDiagnosticsOnOutOfMemoryError -XX:HeapDumpPath=/dumps -XX:+HeapDumpOnCtrlBreak -XX:+HeapDumpOnOutOfMemoryError -Dweblogic.webservice.i18n.charset=utf-8 -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -Djava.awt.headless=true -Duser.language=ru -Duser.country=RU')

#PSRV Cluster
cd('/Servers/wl_by_' + ENV + '_01_psrv/ServerStart/wl_by_' + ENV + '_01_psrv')
cmo.setArguments('-Xms256m -Xmx256m -Xmanagement:port=5906 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Dweblogic.Stdout=/log/fmw/managedservers/wl_by_' + ENV + '_01_psrv/stdout.log -Dweblogic.Stderr=/log/fmw/managedservers/wl_by_' + ENV + '_01_psrv/stderr.log -Xverbose:gc=info,memory=info -XverboseLog:/log/fmw/managedservers/wl_by_' + ENV + '_01_psrv/jrockit.log -XX:+HeapDiagnosticsOnOutOfMemoryError -XX:HeapDumpPath=/dumps -XX:+HeapDumpOnCtrlBreak -XX:+HeapDumpOnOutOfMemoryError -Dweblogic.webservice.i18n.charset=utf-8 -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -Djava.awt.headless=true -Duser.language=ru -Duser.country=RU')

cd('/Servers/wl_by_' + ENV + '_02_psrv/ServerStart/wl_by_' + ENV + '_02_psrv')
cmo.setArguments('-Xms256m -Xmx256m -Xmanagement:port=5906 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Dweblogic.Stdout=/log/fmw/managedservers/wl_by_' + ENV + '_02_psrv/stdout.log -Dweblogic.Stderr=/log/fmw/managedservers/wl_by_' + ENV + '_02_psrv/stderr.log -Xverbose:gc=info,memory=info -XverboseLog:/log/fmw/managedservers/wl_by_' + ENV + '_02_psrv/jrockit.log -XX:+HeapDiagnosticsOnOutOfMemoryError -XX:HeapDumpPath=/dumps -XX:+HeapDumpOnCtrlBreak -XX:+HeapDumpOnOutOfMemoryError -Dweblogic.webservice.i18n.charset=utf-8 -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8 -Djava.awt.headless=true -Duser.language=ru -Duser.country=RU')

save()
activate()
print '==> Startup arguments has been changed Finished ... Please check from AdminConsole...'
disconnect()