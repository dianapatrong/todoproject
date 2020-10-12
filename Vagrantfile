# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # Do not pay attention to this parameter
  if Vagrant.has_plugin?("vagrant-vbguest")
    config.vm.provider :virtualbox do |vb|
      config.vbguest.auto_update = true
    end
  end
  config.vm.define "todo_server" do |server|
    # Specify the Vagrant box to use
    server.vm.box = "centos/7"
    # Specify the VM ip address
    server.vm.network :private_network, ip: "20.20.20.2"
    config.vm.network "forwarded_port", guest: 22, host: 2222, host_ip: "127.0.0.1", id: 'ssh'
    # Sync playbooks in current folder with /vagrant folder in guest
    config.vm.synced_folder ".", "/vagrant", type: "virtualbox"
    config.vm.provider "vmware_desktop" do |vmware|
      vmware.vmx["memsize"] = "2048"
      vmware.vmx["numvcpus"] = "1"
    end
  end


  # Use Vagrant Ansible provisioner
  config.vm.provision "ansible_local" do |ansible|
    # The path to the playbooks entry point
    ansible.playbook = "iac/run.yml"
    # Only run the roles with these tags
    ansible.tags = "install"
  end

end