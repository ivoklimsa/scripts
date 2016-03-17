#!/usr/bin/env bash

#Replace example.local with your domain
#Replace user.name(s) with list of admin users

#For enabling debuging remove # from below line
#set -x
version=1.0.0
admins=("user.name" "user.name" "user.name" )
ident=$(hostname -s)
finfo="/etc/info"

if [ -f "$finfo" ]
then
	echo "$(tput bold)$(tput setaf 1)File ${finfo} found.$(tput sgr 0)"
	cat $finfo
	exit 1
else
    echo "$(tput bold)$(tput setaf 2)Configuring server $(tput sgr 0)"
fi

random-string(){
    #Generating password for users
    cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 16 | head -n 1
}

install_packages (){
    #Updating system to latest
    echo "$(tput bold)$(tput setaf 2)Updating system $(tput sgr 0)"
    rm -fr /var/cache/yum/*
    yum clean all
    yum update -y
    yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    echo "$(tput bold)$(tput setaf 2)Installing additional packages $(tput sgr 0)"
    yum install -y net-snmp-utils.x86_64 iproute.x86_64 traceroute.x86_64 mlocate mc nmap bind-utils telnet net-tools \
         net-snmp.x86_64 wget mailx.x86_64 rsync screen unzip glibc.i686 libgcc.i686 libX11.i686 unzip lnav lsof.x86_64 htop.x86_64 ntp.x86_64
}

disable_selinux () {
    #Disabling Selinux
    echo "$(tput bold)$(tput setaf 2)Disabling Selinux $(tput sgr 0)"
    sed -i 's/enforcing/disabled/g' /etc/selinux/config
}

stop_start () {
    #Disabling Firewall and enabling SNMPD
    echo "$(tput bold)$(tput setaf 2)Disabling  Firewall $(tput sgr 0)"
    systemctl disable firewalld
    systemctl stop firewalld
    echo "$(tput bold)$(tput setaf 2)Enabling SNMPD $(tput sgr 0)"
    systemctl enable snmpd.service
    systemctl start snmpd.service
    echo "$(tput bold)$(tput setaf 2)Enabling NTPD $(tput sgr 0)"
    systemctl enable ntpd.service
    systemctl start ntpd.service
}

config_snmp () {
    #Adding community for Orion monitoring
    echo "$(tput bold)$(tput setaf 2)Adding SNMP community for Orion monitoring $(tput sgr 0)"
    echo "rocommunity \$tCroix!!" > /etc/snmp/snmpd.conf
}

config_bash () {
    #Changing default bash color
    echo "$(tput bold)$(tput setaf 2)Changing default bash color. $(tput sgr 0)"
    echo "PS1='\[\e[1;32m\][\u@\h \W]\$\[\e[0m\] '" >> /etc/skel/.bashrc
    echo "PS1='\[\e[1;31m\][\u@\h \W]\$\[\e[0m\] '" >> /root/.bashrc
}

config_mail () {
    #Setting smtp relay
    echo "$(tput bold)$(tput setaf 2)Setting SMTP relay $(tput sgr 0)"
    echo "relayhost = smtp.example.local" > /etc/postfix/main.cf
    echo "mynetworks = 127.0.0.1" >> /etc/postfix/main.cf
    systemctl restart postfix
}

create_groups () {
    #Adding groups
    echo "$(tput bold)$(tput setaf 2)Adding administrators and monitors group $(tput sgr 0)"
    groupadd administrators
    groupadd monitors
}

create_sudoers () {
    #Adding administrators group to sudoers (be able act as root)
    echo "$(tput bold)$(tput setaf 2)Adding administrators group to sudoers (be able act as root)$(tput sgr 0)"
    echo "## Allows people in group administrators act as root" >> /etc/sudoers.d/administrators
    echo "%administrators        ALL=(ALL)       ALL" >> /etc/sudoers.d/administrators
}

create_monitoring_user () {
    #Adding user Orion for monitoring
    echo "$(tput bold)$(tput setaf 2)Adding user for monitoring $(tput sgr 0)"
    useradd -n  -g users -c "User for script based monitoring" orion
    echo password1 | passwd orion --stdin
    usermod -g monitors orion

}
create_admins () {
    #Creating Administrators
    echo "$(tput bold)$(tput setaf 2)Creating Administrators $(tput sgr 0)"
    for admin in "${admins[@]}" ;
        do
            pass=$(random-string)
            useradd -n  -g administrators -c "${admin}@example.local DevOps Administrator" ${admin}
            echo ${pass} | passwd ${admin} --stdin
            chage -d 0 ${admin}
            echo -e "New credentials has been generated for you. \nLogin: ${admin} \nPassword: ${pass} \nServer: ${ident} " | mailx -r "noreplay@example.local" -s "Password for ${ident} " "${admin}@example.local"
        done
}

config_sshd () {
    #Denying root to login via ssh, allowing ssh for administrator, monitor groups
    echo "$(tput bold)$(tput setaf 2)Denying root to login via ssh, allowing ssh for administrator, monitor groups $(tput sgr 0)"
    echo "# Prevent root logins:" >> /etc/ssh/sshd_config
    echo "PermitRootLogin no" >> /etc/ssh/sshd_config
    echo "# Allow only specific users to ssh to this VM" >> /etc/ssh/sshd_config
    echo "AllowGroups administrators monitors" >> /etc/ssh/sshd_config
    systemctl restart sshd.service
}

generate_info () {
    #Generate information when, from which ip and who run this script
    echo "$(tput bold)$(tput setaf 2)Generate information when, from which ip and who run this script $(tput sgr 0)"
    echo "#Version" >> /etc/info
    echo $version >> /etc/info
    echo "Timestamp" >> /etc/info
    date >> /etc/info
    echo  "#Username" >> /etc/info
    echo $USER >> /etc/info
    echo  "#SourceIP" >> /etc/info
    echo $SSH_CLIENT | awk '{ print $1 }' >> /etc/info

}

install_packages
disable_selinux
config_snmp
stop_start
config_bash
config_mail
create_groups
create_sudoers
create_monitoring_user
create_admins
config_sshd
generate_info

echo "$(tput bold)$(tput setaf 2)Success! $(tput sgr 0)"
echo "$(tput bold)$(tput setaf 2)Rebooting server $(tput sgr 0)"
reboot

exit 0
