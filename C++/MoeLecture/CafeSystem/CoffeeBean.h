#pragma once

class CoffeeBean
{
public:
	CoffeeBean( const char *_name, int price );
	~CoffeeBean();

public:
	void Disyplay();

public:
	inline char* GetName() { return name; }
	inline int GetPrice() { return price; }

private:
	char *name;
	int price;
};

