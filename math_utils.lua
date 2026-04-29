local M = {}

function M.add(left, right)
    return left + right
end

function M.multiply(left, right)
    return left * right
end

function M.greet(name)
    return "hello, " .. name
end

return M

