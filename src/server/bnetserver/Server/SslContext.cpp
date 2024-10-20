/*
 * This file is part of the TrinityCore Project. See AUTHORS file for Copyright information
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation; either version 2 of the License, or (at your
 * option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
 * more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */

#include "SslContext.h"
#include "Log.h"
#include "Config.h"

bool Battlenet::SslContext::_usesDevWildcardCertificate = false;

namespace
{
auto CreatePasswordUiMethodFromPemCallback(::pem_password_cb* callback)
{
    return Trinity::make_unique_ptr_with_deleter(UI_UTIL_wrap_read_pem_callback(callback, 0), &::UI_destroy_method);
}

auto OpenOpenSSLStore(boost::filesystem::path const& storePath, UI_METHOD const* passwordCallback, void* passwordCallbackData)
{
    std::string uri;
    uri.reserve(6 + storePath.size());

    uri += "file:";
    std::string genericPath = storePath.generic_string();
    if (!genericPath.empty() && !genericPath.starts_with('/'))
        uri += '/'; // ensure the path starts with / (windows special case, unix absolute paths already do)

    uri += genericPath;

    return Trinity::make_unique_ptr_with_deleter(OSSL_STORE_open(uri.c_str(), passwordCallback, passwordCallbackData, nullptr, nullptr), &::OSSL_STORE_close);
}

boost::system::error_code GetLastOpenSSLError()
{
    auto ossl_error = ::ERR_get_error();
    if (ERR_SYSTEM_ERROR(ossl_error))
        return boost::system::error_code(static_cast<int>(::ERR_GET_REASON(ossl_error)), boost::asio::error::get_system_category());

    return boost::system::error_code(static_cast<int>(ossl_error), boost::asio::error::get_ssl_category());
}
}

bool Battlenet::SslContext::Initialize()
{
    boost::system::error_code err;

#define LOAD_CHECK(fn) do { fn; \
    if (err) \
    { \
        TC_LOG_ERROR("server.ssl", #fn " failed: %s", err.message().c_str()); \
        return false; \
    } } while (0)

    std::string certificateChainFile = sConfigMgr->GetStringDefault("CertificatesFile", "./bnetserver.cert.pem");
    std::string privateKeyFile = sConfigMgr->GetStringDefault("PrivateKeyFile", "./bnetserver.key.pem");

    LOAD_CHECK(instance().set_options(boost::asio::ssl::context::no_sslv3, err));
    LOAD_CHECK(instance().use_certificate_chain_file(certificateChainFile, err));
    LOAD_CHECK(instance().use_private_key_file(privateKeyFile, boost::asio::ssl::context::pem, err));

#undef LOAD_CHECK

    return true;
}

boost::asio::ssl::context& Battlenet::SslContext::instance()
{
    static boost::asio::ssl::context context(boost::asio::ssl::context::sslv23);
    return context;
}
