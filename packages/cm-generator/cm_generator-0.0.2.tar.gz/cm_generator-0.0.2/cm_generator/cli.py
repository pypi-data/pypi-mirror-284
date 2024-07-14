import argparse

import cm_generator.handler as hand
from cm_generator import __version__

def cli():

    parser = argparse.ArgumentParser(description="Create QR codes and Auro Markers.")
    parser.add_argument('--version', action='version', version=f'CM-Genertaor - v{__version__}')

    codes, marker = hand.get_code_marker()
    
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand', metavar="", description="Available subcommands for Qr-Generator:")


    gen_parser = subparsers.add_parser(
        "generate",
        help="Manages the generation of codes and markers.",
        description="Generate codes and markers with great precision and seemlessly convert it into an image."

    )

    gen_parser.add_argument("Type", help="The type of code to generate or locate.")
    gen_parser.add_argument("--text", metavar="", help="Text to encode in code", default="")
    gen_parser.add_argument("--width", metavar="", type=int, help="Width of the code", default=64)
    gen_parser.add_argument("--height", metavar="", type=int, help="Heigth of the code", default=64)
    gen_parser.add_argument("--q_zone", metavar="", type=int, help="Quiet zone of the code", default=-1)
    gen_parser.add_argument("--e_level", metavar="", type=int, help="Error level of the code", default=-1)
    #
    gen_parser.add_argument("--m-dict", metavar="", help="Marker Dictionary for Aruco marker", default="4x4_1000")
    gen_parser.add_argument("--id", metavar="", type=int, help="The value of id to encode in the Aruco marker.", default=0)
    gen_parser.add_argument("--size", metavar="", type=int, help="size of the Aurco marker", default=20)
    #
    gen_parser.add_argument("--s-vert", metavar="", type=int, help="Count of vertical squares in Charuco board.", default=5)
    gen_parser.add_argument("--s-horz", metavar="", type=int, help="Count of horizontal squares in charuco board", default=7)
    gen_parser.add_argument("--s-len", metavar="", type=int, help="Length of squares in charuco board.", default=30)
    gen_parser.add_argument("--m-len", metavar="", type=int, help="Length of the marker in Charuco board.", default=15)
    gen_parser.add_argument("--margin", metavar="", type=int, help="Margin for the Charuco board.", default=5)
    #
    gen_parser.add_argument("--dest", metavar="", help="Destination folder of the code or marker", default=".")
    gen_parser.add_argument("--name", metavar="", help="Filename of the code or marker", default="my.png")
    gen_parser.add_argument("--location", action="store_true", help="To save the location of the code or marker", default=False)
    gen_parser.add_argument("--no-save", action="store_false", help="Don't save the code or marker")


    loc_parser = subparsers.add_parser(
        "locate",
        help="Manages the locating of the codes and markers.",
        description="Locating codes and markers with great precision and seamlessly format the location in a structured format."
    )

    loc_parser.add_argument("Type", help="Type to detect", choices=["code", "marker"])
    loc_parser.add_argument("file_path", help="File path of the file to locate code or marker.")
    loc_parser.add_argument("--m-dict", metavar="", help="Marker Dictionary for Aruco marker", default="4x4_50")
    loc_parser.add_argument("--dest", metavar="", help="Destination folder of the code or marker", default=".")
    loc_parser.add_argument("--name", metavar="", help="Filename of the code or marker", default="my")
    loc_parser.add_argument("--save", action="store_true", help="Don't save the code or marker")





    args = parser.parse_args()


    if args.subcommand == "generate":

        if args.Type not in codes and args.Type not in marker:
            raise argparse.ArgumentError(argparse.Action([], "Type"), f"invalid choice: '{args.Type}' (choose from {', '.join([f'{i}' for i in list(codes)[:-3]+marker])})")

        elif args.Type in codes:
            
            res = hand.QR_gen(args.Type, args.text, args.width, args.height, args.q_zone, args.e_level,
                        args.dest, args.name, args.location, args.no_save)
            
            if isinstance(res, tuple):
                print("Code Location : ", res[1])

        elif args.Type in marker and args.Type == "aruco":
            hand.aru_gen(args.m_dict, args.id, args.size, args.dest, args.name, args.no_save)

        elif args.Type in marker and args.Type == "charuco":
            hand.charu_gen(args.m_dict, args.s_vert, args.s_horz, args.s_len, args.m_len, args.id, args.size, args.margin,
                           args.dest, args.name, args.no_save)

    
    elif args.subcommand == "locate":
        
        if args.Type == "code":
            res = hand.QR_loc(args.file_path, args.save, args.dest, args.name)
        
            if isinstance(res, list):
                print(res)
        

        elif args.Type == "marker":
            res = hand.aru_loc(args.file_path, args.m_dict, args.save, args.dest, args.name)

            if isinstance(res, list):
                print(res)