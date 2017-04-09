# -*- mode: ruby -*-
# vi: set ft=ruby :

hosts = {
  "loadbalancer" => "192.168.33.10",
  "app1" => "192.168.33.11",
  "app2" => "192.168.33.12",
  "db" => "192.168.33.13"
}

Vagrant.configure("2") do |config|
  hosts.each do |name, ip|
    config.vm.define name do |machine|
	config.vm.provision "shell", inline: <<-SHELL
        echo "ubuntu:ubuntu" | sudo chpasswd
      SHELL
	  config.vm.provision "shell", inline: <<-SHELL
        apt install python -y
      SHELL
      machine.vm.box = "ubuntu/xenial64"
      machine.vm.hostname = "%s.example.org" % name
      machine.vm.network :private_network, ip: ip
      machine.vm.provider "virtualbox" do |v|
          v.name = name
          #v.customize ["modifyvm", :id, "--memory", 200]
          #v.customize ["modifyvm", :id, "--nictype1", "Am79C973"]
          #v.customize ["modifyvm", :id, "--nictype2", "Am79C973"]
      end
    end
  end
end

