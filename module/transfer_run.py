def get_transfer_run(state, client, parent):

    runs = client.list_transfer_runs(parent=parent)
    total_runs_count = 0
    failed_runs_names = []
    for r in runs:
        total_runs_count += 1
        if str(r.state) == state:
            failed_runs_names.append(r.name)

    deleted_transfers_count = delete_transfer_runs(client, failed_runs_names)
    return (total_runs_count, deleted_transfers_count)


def delete_transfer_runs(client, names):
    counter = 0
    print("Got the following runs:")
    for name in names:
        counter += 1
        client.delete_transfer_run(name=name)
        print(f'run {name} was deleted')

    return counter
