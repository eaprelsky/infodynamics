#!/usr/bin/env python3
"""
Information Dynamics CLI Tool

Command-line interface for calculating information flow parameters.

Usage examples:
    python cli.py conductivity --working_memory 7.5 --attention 0.8 --motivation 0.9
    python cli.py flow_rate --voltage 8.5 --conductivity 6.2
    python cli.py analyze_user --profile expert
    python cli.py analyze_content --text "Breaking news: Important announcement"
"""

import argparse
import json
import sys
import os

# Add parent directory to path to import infodynamics
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import infodynamics as id


def cmd_conductivity(args):
    """Calculate information conductivity for a user."""
    
    profile = {
        "working_memory": args.working_memory,
        "attention_selectivity": args.attention,
        "motivation": args.motivation,
        "expertise": args.expertise,
        "processing_speed": getattr(args, 'processing_speed', 0.7)
    }
    
    context = None
    if hasattr(args, 'distraction') and args.distraction is not None:
        context = {
            "distraction_level": args.distraction,
            "time_pressure": getattr(args, 'time_pressure', 0.0),
            "fatigue": getattr(args, 'fatigue', 0.0)
        }
    
    try:
        G_info = id.calculate_g_info(profile, context)
        
        print(f"📊 Information Conductivity Analysis")
        print(f"=" * 40)
        print(f"👤 User Profile:")
        for key, value in profile.items():
            print(f"   {key.replace('_', ' ').title()}: {value}")
        
        if context:
            print(f"🌍 Context:")
            for key, value in context.items():
                print(f"   {key.replace('_', ' ').title()}: {value}")
        
        print(f"\n⚡ Results:")
        print(f"   G_info = {G_info:.2f}")
        print(f"   R_info = {1/G_info:.2f} (resistance)")
        
        # Interpretation
        if G_info > 7:
            print(f"   ✅ Excellent information reception capability")
        elif G_info > 5:
            print(f"   ✅ Good information reception capability")
        elif G_info > 3:
            print(f"   ⚠️  Average information reception capability")
        else:
            print(f"   ❌ Poor information reception capability")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


def cmd_flow_rate(args):
    """Calculate information flow rate."""
    
    try:
        flow = id.calculate_flow_rate(args.voltage, args.conductivity)
        
        print(f"🌊 Information Flow Analysis")
        print(f"=" * 40)
        print(f"📊 Input Parameters:")
        print(f"   Voltage (U_info): {args.voltage:.2f}")
        print(f"   Conductivity (G_info): {args.conductivity:.2f}")
        
        print(f"\n⚡ Results:")
        print(f"   Flow Rate (V_info): {flow:.2f}")
        
        # Interpretation
        if flow > 50:
            print(f"   🚀 Very fast information processing")
        elif flow > 25:
            print(f"   ✅ Good information processing speed")
        elif flow > 10:
            print(f"   ⚠️  Moderate information processing speed")
        else:
            print(f"   🐌 Slow information processing")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
        
    return 0


def cmd_analyze_user(args):
    """Analyze user with preset profile."""
    
    from infodynamics.models.conductivity import PRESET_PROFILES
    
    if args.profile not in PRESET_PROFILES:
        print(f"❌ Unknown profile: {args.profile}")
        print(f"Available profiles: {list(PRESET_PROFILES.keys())}")
        return 1
    
    profile = PRESET_PROFILES[args.profile]
    
    try:
        G_info = id.calculate_g_info(profile)
        R_info = id.calculate_r_info(profile)
        L_info = id.calculate_l_info(profile)
        C_info = id.calculate_c_info(profile)
        
        print(f"👤 User Profile Analysis: {args.profile}")
        print(f"=" * 50)
        
        print(f"📋 Profile Parameters:")
        for key, value in profile.items():
            print(f"   {key.replace('_', ' ').title()}: {value}")
        
        print(f"\n⚡ Information Dynamics:")
        print(f"   G_info (Conductivity): {G_info:.2f}")
        print(f"   R_info (Resistance):   {R_info:.2f}")
        print(f"   L_info (Inductance):   {L_info:.2f}")
        print(f"   C_info (Capacity):     {C_info:.2f}")
        
        # Calculate optimal content voltage
        optimal_voltage = 30 / G_info  # Target flow rate of 30
        print(f"\n🎯 Recommendations:")
        print(f"   Optimal content voltage: {optimal_voltage:.2f}")
        if optimal_voltage < 5:
            print(f"   💡 User can handle high-quality complex content")
        elif optimal_voltage < 8:
            print(f"   💡 User prefers good-quality standard content")
        else:
            print(f"   💡 User needs simple, clear content")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
        
    return 0


def cmd_analyze_content(args):
    """Analyze content voltage."""
    
    # Simple content analysis (placeholder)
    text = args.text
    content_profile = {
        "factual_density": min(1.0, len(text.split()) / 50),  # Word density
        "credibility": 0.8 if "research" in text.lower() or "study" in text.lower() else 0.6,
        "semantic_quality": 0.7,  # Placeholder
        "timeliness": 0.9 if "breaking" in text.lower() or "new" in text.lower() else 0.5
    }
    
    try:
        U_info = id.calculate_u_info(content_profile)
        
        print(f"📄 Content Analysis")
        print(f"=" * 40)
        print(f"📝 Text: \"{text[:50]}{'...' if len(text) > 50 else ''}\"")
        
        print(f"\n📊 Content Profile:")
        for key, value in content_profile.items():
            print(f"   {key.replace('_', ' ').title()}: {value:.2f}")
        
        print(f"\n⚡ Results:")
        print(f"   U_info (Voltage): {U_info:.2f}")
        
        # Interpretation
        if U_info > 8:
            print(f"   🔥 High-impact content")
        elif U_info > 6:
            print(f"   ✅ Good-quality content")
        elif U_info > 4:
            print(f"   ⚠️  Average content")
        else:
            print(f"   📝 Basic content")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
        
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Information Dynamics CLI Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s conductivity --working_memory 7.5 --attention 0.8 --motivation 0.9 --expertise 0.6
  %(prog)s flow_rate --voltage 8.5 --conductivity 6.2
  %(prog)s analyze_user --profile expert
  %(prog)s analyze_content --text "Breaking news about AI research"
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Conductivity command
    parser_g = subparsers.add_parser('conductivity', help='Calculate information conductivity')
    parser_g.add_argument('--working_memory', type=float, required=True, 
                         help='Working memory capacity (0-10)')
    parser_g.add_argument('--attention', type=float, required=True,
                         help='Attention selectivity (0-1)')
    parser_g.add_argument('--motivation', type=float, required=True,
                         help='Motivation level (0-1)')
    parser_g.add_argument('--expertise', type=float, required=True,
                         help='Domain expertise (0-1)')
    parser_g.add_argument('--processing_speed', type=float, default=0.7,
                         help='Processing speed (0-1)')
    parser_g.add_argument('--distraction', type=float,
                         help='Distraction level (0-1)')
    parser_g.add_argument('--time_pressure', type=float, default=0.0,
                         help='Time pressure (0-1)')
    parser_g.add_argument('--fatigue', type=float, default=0.0,
                         help='Fatigue level (0-1)')
    
    # Flow rate command
    parser_f = subparsers.add_parser('flow_rate', help='Calculate information flow rate')
    parser_f.add_argument('--voltage', type=float, required=True,
                         help='Information voltage (0-10)')
    parser_f.add_argument('--conductivity', type=float, required=True,
                         help='Information conductivity (0-10)')
    
    # User analysis command
    parser_u = subparsers.add_parser('analyze_user', help='Analyze user with preset profile')
    parser_u.add_argument('--profile', type=str, required=True,
                         choices=['expert', 'student', 'casual_user', 'overloaded'],
                         help='User profile type')
    
    # Content analysis command
    parser_c = subparsers.add_parser('analyze_content', help='Analyze content voltage')
    parser_c.add_argument('--text', type=str, required=True,
                         help='Content text to analyze')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Route to appropriate command
    commands = {
        'conductivity': cmd_conductivity,
        'flow_rate': cmd_flow_rate,
        'analyze_user': cmd_analyze_user,
        'analyze_content': cmd_analyze_content
    }
    
    return commands[args.command](args)


if __name__ == '__main__':
    sys.exit(main()) 