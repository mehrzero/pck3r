#!/usr/bin/ruby
require './library_requirements/requirement'
require 'fileutils'
sys_status("start_install")
Dir.chdir("/root") do
  if Dir.exists?".minecraft"# rm /root/.minecraft"
    puts "#{FileUtils.rm_rf(".minecraft")}".green
    sys_status("not_error")
  else
    puts "'/root/.minecraft ' directory  not found".red
  end
end
