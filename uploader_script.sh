for f in *; do
    if [ -d "$f" ]; then
        fname=$(basename "$f")
        python3 uploader.py --raw_data_dir "$fname"
    fi
done