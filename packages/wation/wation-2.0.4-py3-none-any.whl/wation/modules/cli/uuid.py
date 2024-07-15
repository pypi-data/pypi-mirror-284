import uuid as uuid_module
import sys

def main(args):
    try:
        quantity = args.quantity
        version = args.version
        uuids = []

        if sys.stdout.isatty():
            print(f"[+] Generated {quantity} UUID(s) of version {version}\n")

        for idx in range(quantity):
            if version == 1:
                uuid = uuid_module.uuid1()
            elif version == 3:
                if not args.namespace:
                    raise ValueError("Namespace (-n) is required for UUID version 3.")
                uuid = uuid_module.uuid3(uuid_module.NAMESPACE_DNS, args.namespace)
            elif version == 4:
                uuid = uuid_module.uuid4()
            elif version == 5:
                if not args.namespace:
                    raise ValueError("Namespace (-n) is required for UUID version 5.")
                uuid = uuid_module.uuid5(uuid_module.NAMESPACE_DNS, args.namespace)
            else:
                raise ValueError(f"Unsupported UUID version: {version}")

            uuid_str = str(uuid)

            if args.output:
                with open(args.output, 'a' if idx > 0 else 'w') as f:
                    f.write(uuid_str + '\n')
            else:
                if args.output is None and sys.stdout.isatty():
                    print(f"{idx + 1:02d}. {uuid_str}")
                else:
                    print(uuid_str)
                    uuids.append(uuid_str)

    except ValueError as e:
        print(f"[-] Error: {str(e)}")