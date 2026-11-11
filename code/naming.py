def get_model_file(args):
    model_file = '[epochs{}][alpha{}][anchor{}][max_sample{}][emb{}][lr{}][batchsize{}][topk{}]'.format(args.epochs, args.alpha, args.anchor, args.sample_max_path_len, args.embedding_size, args.learning_rate, args.batch_size, args.get_top_k)
    return model_file
