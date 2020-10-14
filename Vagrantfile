# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # Do not pay attention to this parameter
  if Vagrant.has_plugin?("vagrant-vbguest")
    config.vm.provider :virtualbox do |vb|
      config.vbguest.auto_update = true
      vb.customize ["modifyvm", :id, "--name", "todolist-app", "--memory", "1024"]
    end
  end
  config.vm.provision "file", source: ".", destination: "$HOME/todoproject"
  config.vm.define "todolist-app" do |server|
    server.vm.box = "ubuntu/bionic64"
    server.vm.hostname = "todolist-app"
    server.vm.network :private_network, ip: "20.20.20.2"
    server.vm.network "forwarded_port", guest: 8000, host: 8080, host_ip: "127.0.0.1"
    config.vm.provider "vmware_desktop" do |vmware|
      vmware.vmx["memsize"] = "2048"
      vmware.vmx["numvcpus"] = "1"
    end
  end

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "iac/run.yml"
    ansible.tags = "install"
  end

end