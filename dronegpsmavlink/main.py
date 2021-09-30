import asyncio
from mavsdk import System

#Run these commands in the terminal to start simulation, also open qground control to connect
# # Navigate to PX4-Autopilot repo
# cd PX4-Autopilot
# # Build and runs SITL simulation with jMAVSim to test the setup
# make px4_sitl jmavsim

async def run():
    # Init the drone
    drone = System()
    await drone.connect()
    print('banana')
    # Start the tasks
    asyncio.ensure_future(print_battery(drone))
    print('banana')
    asyncio.ensure_future(print_gps_info(drone))
    asyncio.ensure_future(print_in_air(drone))
    asyncio.ensure_future(print_position(drone))

async def print_battery(drone):
    print('banana')
    async for battery in drone.telemetry.battery():
        print(f"Battery: {battery.remaining_percent}")


async def print_gps_info(drone):
    async for gps_info in drone.telemetry.gps_info():
        print(f"GPS info: {gps_info}")


async def print_in_air(drone):
    async for in_air in drone.telemetry.in_air():
        print(f"In air: {in_air}")


async def print_position(drone):
    async for position in drone.telemetry.position():
        print(position)


if __name__ == "__main__":
    # Start the main function
    asyncio.ensure_future(run())

    # Runs the event loop until the program is canceled with e.g. CTRL-C
    asyncio.get_event_loop().run_forever()