#include <Windows.h>
#include "Time.h"


using namespace DX12PE;
using namespace Helper;


DATETIME Time::TryMilliSecParse(unsigned __int64 milliseconds)
{
	if (0 >= milliseconds)
		return DATETIME();

	int year	= milliseconds / millisecPerYear;
	int day		= (milliseconds % millisecPerYear) / millisecPerDay;
	int hour	= (milliseconds % millisecPerDay) / millisecPerHour;
	int min		= (milliseconds % millisecPerHour) / millisecPerMin;
	int sec		= (milliseconds % millisecPerMin) / milliseconds;

	return DATETIME(year, day, hour, min, sec);
}

__int64	Time::GetSystemTickCount()
{
	__int64 tick;
	QueryPerformanceCounter((LARGE_INTEGER*)&tick);
	return tick;
}


Clock::Clock() 
	:secondsPerCount(0.0),
	deltaTime(0.0),
	mainTick(0),
	pausedTick(0),
	stopTick(0),
	curTick(0),
	prevTick(0),
	isStop(false)
{

	__int64 countsPerSeconds;
	QueryPerformanceFrequency((LARGE_INTEGER*)&countsPerSeconds);

	secondsPerCount		= 1.0 / (double)countsPerSeconds;
}


void Clock::TickTock()
{
	if (isStop)
	{
		deltaTime = 0.0;
		return;
	}

	curTick		= Time::GetSystemTickCount();
	deltaTime	= (curTick - prevTick) * secondsPerCount;
	prevTick	= curTick;

	if (0.0 > deltaTime)
		deltaTime = 0.0;
}

void Clock::Reset()
{
	mainTick	= Time::GetSystemTickCount();
	prevTick	= mainTick;
	stopTick	= 0;
	isStop		= false;
}

void Clock::Start()
{
	if (false == isStop)
		return;

	__int64 tick = Time::GetSystemTickCount();

	pausedTick += tick - stopTick;
	prevTick	= tick;
	stopTick	= 0;
	isStop		= false;
}

void Clock::Stop()
{
	if (true == isStop)
		return;

	stopTick	= Time::GetSystemTickCount();
	isStop		= true;
}

float Clock::TotalTime() const
{
	if (isStop)
	{
		return (float)(((stopTick - pausedTick) - mainTick) * secondsPerCount);
	}
	else
	{
		return (float)(((curTick - pausedTick) - mainTick) * secondsPerCount);
	}
}