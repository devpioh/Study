#include "pch.h"
#include "SimpleWin.h"

LRESULT CALLBACK InitWin::MsgProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
    PAINTSTRUCT ps;
    HDC hdc;

    std::wstring message = L"Hello Window!";

    switch(msg)
    {
        case WM_PAINT:
            hdc = BeginPaint(hWnd, &ps);
            TextOut(hdc, 5, 5, message.c_str(), message.size());
            EndPaint(hWnd, &ps);
            break;

        case WM_DESTROY:
            PostQuitMessage(0);
            break;
        
        default:
            return DefWindowProc(hWnd, msg, wParam, lParam);
    }

    return 0;
}