#pragma once

namespace DX12PE
{
	namespace Helper
	{
		inline bool HasFlag(unsigned __int64 target, unsigned __int64 flag)
		{
			return 0 != (target & flag);
		}

		inline std::wstring AnsiToWString(const std::string& str)
		{
			WCHAR buffer[512];
			MultiByteToWideChar(CP_ACP, 0, str.c_str(), -1, buffer, 512);
			return std::wstring(buffer);
		}
	}
}