for i in /home/diamondman/adapt\ stuff/waveforms/images/* ; do                                                                                                                        
  if [ -d "$i" ]; then
    convert $i/base.png -fill red -pointsize 30 -annotate +575+36 0x${(U)$(basename "$i")} $i/base_name.png
  fi
done

