#pragma once

namespace DX12PE
{
	struct DATETIME
	{
		int seconds;
		int minute;
		int hour;
		int day;
		int year;

		DATETIME() : seconds(0), minute(0), hour(0), day(0), year(0)
		{
		}

		DATETIME(int _year, int _day, int _hour, int _min, int _sec) :
			year(_year), day(_day), hour(_hour), minute(_min), seconds(_sec)
		{
		}

		inline bool IsZero() { return 0 >= seconds && 0 >= minute && 0 >= hour && 0 >= day && 0 >= year; }
	};


	class Clock
	{
	public:
		Clock();

		void Reset();
		void Start();
		void Stop();
		void TickTock();

		float TotalTime() const;
		inline float DeltaTime() const { return (float)deltaTime; }

	private:
		double secondsPerCount;
		double deltaTime;

		__int64	mainTick;
		__int64 pausedTick;
		__int64 stopTick;
		__int64 curTick;
		__int64 prevTick;

		bool isStop;
	};


	namespace Helper
	{
		namespace Time
		{
			constexpr unsigned __int64 milliseconds		= 1000;
			constexpr unsigned __int64 millisecPerMin	= milliseconds * 60;
			constexpr unsigned __int64 millisecPerHour	= millisecPerMin * 60;
			constexpr unsigned __int64 millisecPerDay	= millisecPerHour * 24;
			constexpr unsigned __int64 millisecPerYear	= millisecPerDay * 365;

			DATETIME TryMilliSecParse(unsigned __int64 milliseconds);

			__int64 GetSystemTickCount();
		}
	}
}

