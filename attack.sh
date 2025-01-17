mode=$1

CUDA_VISIBLE_DEVICES=0 python3 cold_decoding.py  \
	--seed 2025 \
	--mode $mode \
	--pretrained_model Llama-2-7b-chat-hf \
	--init-temp 1 \
    --length 20 \
	--max-length 20 \
	--num-iters 2000 \
	--min-iters 0 \
	--goal-weight 100 \
    --rej-weight 100 \
	--stepsize 0.1 \
	--noise-iters 1 \
	--win-anneal-iters 1000 \
	--start 32 \
	--end 50 \
	--lr-nll-portion 1.0 \
    --topk 10 \
    --output-lgt-temp 1 \
	--verbose \
    --straight-through  \
	--large-noise-iters 50,200,500,1500\
	--large_gs_std  0.1,0.05,0.01,0.001  \
	--stepsize-ratio 1  \
    --batch-size 8 \
    --print-every 1000 \
	--fp16 
	
